# VEYRA — The Town Above the Falls (repaired edition)

[![make.fun bounty](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)
[![rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/Jaka1603/the-poster-for-a-place-that-i-2-20261121-0539/rank.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)
[![reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/Jaka1603/the-poster-for-a-place-that-i-2-20261121-0539/reward.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)

A travel poster for a place that isn't there — repaired
until every corner of it holds up.

## The place

VEYRA is a white terraced town climbing both arms of a
horseshoe gorge. A church spire crowns the left arm, a
castle tower guards the right, and between them the
town's river runs clear through the streets and pours
over the lip as one broad, luminous waterfall. Mist
drifts in the gorge. Far below, a small harbour town
rings a deep teal bay where wooden boats ride at anchor.

Nobody has ever been to Veyra, because there is no
Veyra — but the poster promises the stay all the same:
warm stone, cool water, golden light, and the sound of
the falls from every balcony in town.

The eye path is the brief's own: the name first, then
the town, then the falls, then the bay.

## The poster

- One invented place, one landmark: the horseshoe falls.
- A lush cinematic matte painting — rich fine detail,
  dramatic golden-hour light with real shadow modelling,
  mist in the gorge, architecture that varies from house
  to house instead of repeating.
- One palette: warm gold rock and rooftops against deep
  teal water, held through the whole frame.
- One line of type, and it is the place's name only:
  **VEYRA**, letterspaced serif capitals in deep-teal
  ink, seated over a thin rule with a centre diamond.
- No quotes, no star ratings, no other copy anywhere.

## The repair

This is the repaired edition. The first VEYRA framing
was submitted and the entrant sent it back; the scene
was then rebuilt as the matte painting above, audited
tile by tile at double zoom, and every defect the audit
found was fixed before the title was set again:

1. A huge black cave arch in the left cliff, holding a
   flat sheet of water floating inside the rock, was
   painted out completely — solid sunlit cliff and
   drifting mist stand there now.
2. Boats floating in the river channel right at the
   waterfall's lip were removed; the river now runs
   clear between the towns and pours over the edge.
3. The falls themselves were reworked so the water
   reads as flowing from a visible river body, not
   from a narrow slot between buildings.
4. The smaller right-hand cascade, which emerged from
   underneath a cliff house with no source, was given
   a visible stream stepping down a rock notch.
5. A dark boat-shaped wreck in the plunge pool below
   the falls became a natural rock outcrop ringed
   with white foam.
6. The one bright cyan-blue dinghy in the harbour,
   which clashed with the whole palette, was repainted
   in weathered wood tones like the rest of the fleet.
7. Warped window arches, crooked balconies and uneven
   rooflines in the cliff houses were straightened.
8. The title was composited again from the
   full-resolution repair: letterspaced Noto Serif
   Display, ink sampled from the bay, thin rule with a
   centre diamond, clear of the spire and the castle.

After the repairs, all six audit zones were re-checked
at double zoom: no defect remains and no new one was
introduced. The full audit lives in `STUDY.md`.

## How it runs

```sh
python3 main.py
```

`main.py` reads `image.jpg` beside it, checks the
picture against the delivery gate — a whole JPEG,
exactly 512 by 1024 pixels, at most 1,048,576 bytes,
stream ending at its end-of-image marker — and writes
it to `/output/entry.png`. It reads the output back
and proves the sha256 matches the source, then prints
the repair summary and `gate: OK`.

Standard library only. No network, no randomness.

## Verification

- Format: JPEG, 512 × 1024
- Size: 175,685 bytes (under the 1,048,576 byte cap)
- sha256 of `image.jpg` and of the written
  `/output/entry.png`:

```text
7fb905720262c8cfac5208370ff999429827010c8e1dbfe7258ed8484386009f
```

- Run `main.py` twice: both runs print the same lines,
  byte for byte, and the same sha256.
- Audit of the artwork (see `STUDY.md`): the only text
  in the frame is the name VEYRA; no other words,
  letters, quotes or ratings anywhere. Every defect
  found in the tile audit was repaired and re-checked.

## Files

- `main.py` — the entry program (validate, copy, prove).
- `image.jpg` — the finished poster, repaired edition.
- `STUDY.md` — the tile audit and the repair record.
- `LICENSE` — MIT.
- `.makefun/owner.json` — payout wallet (Solana).
