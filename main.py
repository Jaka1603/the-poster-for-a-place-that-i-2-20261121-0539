#!/usr/bin/env python3
"""VEYRA poster entry.

Reads the finished poster image stored beside this file,
checks it against the house gate, and writes it out as
/output/entry.png.

Standard library only. No network, no randomness, no input
besides the image file itself.
"""

import hashlib
import os
import struct
import sys

MAX_BYTES = 1048576
MAX_SIDE = 1024
SOURCE_NAME = "image.jpg"
OUTPUT_PATH = "/output/entry.png"

JPEG_MAGIC = b"\xff\xd8\xff"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print("error:", message, file=sys.stderr)
    raise SystemExit(1)


def read_source():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, SOURCE_NAME)
    try:
        with open(path, "rb") as handle:
            return handle.read()
    except OSError as exc:
        fail("cannot read %s: %s" % (SOURCE_NAME, exc))


def jpeg_size(data):
    # Walk the JPEG markers until a start-of-frame block
    # hands over the picture's width and height.
    pos = 2
    while pos + 9 <= len(data):
        if data[pos] != 0xFF:
            fail("bad JPEG marker at offset %d" % pos)
        marker = data[pos + 1]
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        if pos + 4 > len(data):
            fail("truncated JPEG segment")
        length = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        if length < 2:
            fail("bad JPEG segment length")
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                      0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            if pos + 9 > len(data):
                fail("truncated JPEG frame header")
            height = struct.unpack(">H", data[pos + 5:pos + 7])[0]
            width = struct.unpack(">H", data[pos + 7:pos + 9])[0]
            return width, height
        pos += 2 + length
    fail("no JPEG start-of-frame found")


def png_size(data):
    if len(data) < 24:
        fail("truncated PNG header")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def check_image(data):
    if len(data) == 0:
        fail("image is empty")
    if len(data) > MAX_BYTES:
        fail("image is %d bytes, over the %d byte cap"
             % (len(data), MAX_BYTES))
    if data[:3] == JPEG_MAGIC:
        kind = "JPEG"
        width, height = jpeg_size(data)
    elif data[:8] == PNG_MAGIC:
        kind = "PNG"
        width, height = png_size(data)
    else:
        fail("image is neither JPEG nor PNG")
    if width <= 0 or height <= 0:
        fail("image has no size")
    if width > MAX_SIDE or height > MAX_SIDE:
        fail("image is %dx%d, over the %d px side cap"
             % (width, height, MAX_SIDE))
    return kind, width, height


def write_output(data):
    folder = os.path.dirname(OUTPUT_PATH)
    try:
        os.makedirs(folder, exist_ok=True)
    except OSError as exc:
        fail("cannot make output folder: %s" % exc)
    try:
        with open(OUTPUT_PATH, "wb") as handle:
            handle.write(data)
    except OSError as exc:
        fail("cannot write %s: %s" % (OUTPUT_PATH, exc))
    try:
        with open(OUTPUT_PATH, "rb") as handle:
            written = handle.read()
    except OSError as exc:
        fail("cannot read back %s: %s" % (OUTPUT_PATH, exc))
    if hashlib.sha256(written).hexdigest() != \
            hashlib.sha256(data).hexdigest():
        fail("read-back hash differs from source hash")
    return hashlib.sha256(written).hexdigest()


def main():
    data = read_source()
    kind, width, height = check_image(data)
    digest = write_output(data)
    print("source: %s (%s, %d bytes, %dx%d)"
          % (SOURCE_NAME, kind, len(data), width, height))
    print("wrote: %s (sha256 %s)" % (OUTPUT_PATH, digest))
    print("gate: OK")


if __name__ == "__main__":
    main()
