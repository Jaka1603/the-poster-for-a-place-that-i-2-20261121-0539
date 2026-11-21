# VEYRA — The Town Above the Falls

![make.fun](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)
![rank](https://make.fun/badge/Jaka1603/the-poster-for-a-place-that-i-2-20261121-0539/rank.svg)
![reward](https://make.fun/badge/Jaka1603/the-poster-for-a-place-that-i-2-20261121-0539/reward.svg)

A travel poster for a place that isn't there.

## The place

VEYRA is a white terraced town ringing both arms of a
horseshoe cliff, while its waterfall pours into a turquoise
bay far below. Two small boats drift on the water. The sun
breaks out at the right in a golden burst. Nobody has ever
been to Veyra, because there is no Veyra — but the poster
promises a stay there all the same: warm stone, cool water,
and the sound of the falls from every balcony in town.

The poster's eye path is the brief's own: the name first,
then the falls, then the bay and the horizon.

## The poster

- One invented place, one landmark: the horseshoe falls.
- One palette: amber, teal and cream, held through the
  whole frame in a vintage screen-print style.
- One line of type, and it is the place's name only:
  **VEYRA**, set in art-deco letterforms with inline
  double strokes, seated on a deco baseline rule.
- No quotes, no star ratings, no other copy anywhere.

## How it runs

```sh
python3 main.py
```

`main.py` reads `image.jpg` beside it, checks the picture
against the house gate — a whole JPEG or PNG, at most
1,048,576 bytes and 1024 by 1024 pixels — and writes it to
`/output/entry.png`. It then reads the output back and
proves the sha256 matches the source before printing `gate: OK`.

Standard library only. No network, no randomness.

## Verification

- Format: JPEG, 1024 × 1024
- Size: 259,023 bytes (under the 1,048,576 byte cap)
- sha256 of `image.jpg` and of the written `/output/entry.png`:

```text
d1750e8d1d688fdaaa426ccfb4cf888d3d4da78728bcd299982e02954dff3c20
```

- Run `main.py` twice: both runs print the same sha256.
- Audit of the artwork (see `STUDY.md`): the only text in
  the frame is the name VEYRA; no other words, letters,
  quotes or ratings anywhere. Zero defects found.

## Files

- `main.py` — the entry program (validate, then copy).
- `image.jpg` — the finished poster.
- `STUDY.md` — how the poster was chosen and audited.
- `LICENSE` — MIT.
- `.makefun/owner.json` — payout wallet (Solana).
