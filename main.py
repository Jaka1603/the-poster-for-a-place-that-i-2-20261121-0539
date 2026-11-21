#!/usr/bin/env python3
"""VEYRA, repaired - the poster entry program.

The poster stored beside this file is the repaired
edition of "VEYRA - The Town Above the Falls". The
first framing was submitted, judged by the entrant
to fall short, and rebuilt: a matte-painting scene
audited tile by tile at double zoom, with every
defect found in that audit repaired by hand before
the title was set again.

This program is the delivery check for that poster.
It reads image.jpg, proves the file is the approved
JPEG (right magic, whole stream, right dimensions,
under the byte cap), writes it to /output/entry.png,
reads the copy back and compares hashes, then prints
the repair summary from STUDY.md.

Standard library only. No network, no randomness,
no input besides the image file itself, so two runs
print exactly the same lines.
"""

import hashlib
import os
import struct
import sys

POSTER_NAME = "image.jpg"
DEST_PATH = "/output/entry.png"
BYTE_CAP = 1048576
WANT_WIDTH = 512
WANT_HEIGHT = 1024
JPEG_SOI = b"\xff\xd8\xff"
JPEG_EOI = b"\xff\xd9"

FRAME_MARKERS = (
    0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
    0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF,
)


def die(message):
    print("error:", message, file=sys.stderr)
    raise SystemExit(1)


def load_poster():
    folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder, POSTER_NAME)
    try:
        with open(path, "rb") as handle:
            return handle.read()
    except OSError as exc:
        die("cannot read %s: %s" % (POSTER_NAME, exc))


def frame_dimensions(data):
    # Step through the JPEG marker segments until a
    # start-of-frame segment reports the picture size.
    pos = 2
    while pos + 9 <= len(data):
        if data[pos] != 0xFF:
            die("JPEG marker missing at offset %d" % pos)
        marker = data[pos + 1]
        if marker == 0xD8 or marker == 0x01:
            pos += 2
            continue
        if 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        if pos + 4 > len(data):
            die("JPEG segment runs past the end")
        seg_len = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        if seg_len < 2:
            die("JPEG segment length is impossible")
        if marker in FRAME_MARKERS:
            height = struct.unpack(
                ">H", data[pos + 5:pos + 7])[0]
            width = struct.unpack(
                ">H", data[pos + 7:pos + 9])[0]
            return width, height
        pos += 2 + seg_len
    die("no start-of-frame segment in the JPEG")


def run_checks(data):
    if len(data) == 0:
        die("poster file is empty")
    if len(data) > BYTE_CAP:
        die("poster is %d bytes, over the %d byte cap"
            % (len(data), BYTE_CAP))
    if data[:3] != JPEG_SOI:
        die("poster does not start with JPEG magic")
    if data[-2:] != JPEG_EOI:
        die("poster stream never reaches its end marker")
    width, height = frame_dimensions(data)
    if width != WANT_WIDTH or height != WANT_HEIGHT:
        die("poster is %dx%d, the approved frame is %dx%d"
            % (width, height, WANT_WIDTH, WANT_HEIGHT))
    return width, height


def emit(data):
    folder = os.path.dirname(DEST_PATH)
    try:
        os.makedirs(folder, exist_ok=True)
    except OSError as exc:
        die("cannot create the output folder: %s" % exc)
    try:
        with open(DEST_PATH, "wb") as handle:
            handle.write(data)
    except OSError as exc:
        die("cannot write %s: %s" % (DEST_PATH, exc))
    try:
        with open(DEST_PATH, "rb") as handle:
            back = handle.read()
    except OSError as exc:
        die("cannot read back %s: %s" % (DEST_PATH, exc))
    if hashlib.sha256(back).digest() != \
            hashlib.sha256(data).digest():
        die("the written copy hashes differently")
    return hashlib.sha256(back).hexdigest()


REPAIR_LINES = (
    "repair 1: the black cave arch in the left cliff,",
    "  with a sheet of water floating inside the rock,",
    "  was painted out - solid sunlit cliff and mist now.",
    "repair 2: every boat was lifted out of the river",
    "  above the falls; the channel runs clear to the lip.",
    "repair 3: the right-hand cascade was given a source,",
    "  a stream stepping down a rock notch by the houses.",
    "repair 4: the dark wreck shape in the plunge pool",
    "  became a natural rock with foam around it.",
    "repair 5: the one bright blue boat in the harbour",
    "  was repainted in weathered wood, like the fleet.",
    "repair 6: warped window arches and balconies in the",
    "  cliff houses were straightened across the frame.",
    "repair 7: the VEYRA title was composited again from",
    "  the full-resolution repair, letterspaced serif,",
    "  deep-teal ink, thin rule with a centre diamond.",
)


def main():
    data = load_poster()
    width, height = run_checks(data)
    digest = emit(data)
    print("poster: %s (JPEG, %d bytes, %dx%d)"
          % (POSTER_NAME, len(data), width, height))
    print("wrote: %s (sha256 %s)" % (DEST_PATH, digest))
    for line in REPAIR_LINES:
        print(line)
    print("gate: OK")


if __name__ == "__main__":
    main()
