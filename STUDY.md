# STUDY — the VEYRA repair round

## How this edition came to be

The first VEYRA poster — a flat vintage screen-print —
was submitted to this competition and the entrant
rejected it on sight. A second round in a painterly
gouache style came closer and was still sent back.
The third round changed direction entirely: a lush
cinematic matte painting, rich in fine detail, with
dramatic golden-hour light. That scene won the
entrant's eye — with one instruction attached: check
it again in the smallest detail, and fix every error
and shortcoming found, however small.

This document is the record of that check and of the
repairs it produced. The shipped poster is the
repaired matte painting, nothing else.

## The winning scene

A white terraced town climbs both arms of a horseshoe
gorge: church spire on the left arm, castle tower on
the right, arcaded houses with varied rooflines
between. The town's river runs through the middle and
pours over the lip as a broad luminous waterfall, the
centrepiece of the frame. Mist drifts in the gorge;
below, a harbour town rings a deep teal bay full of
wooden boats. The title sits in the calm sky band at
the top, so the eye runs name, town, falls, bay.

Five candidate scenes were generated and scored
pairwise on detail richness, light drama, composition
and freedom from artefacts. The frontal golden-hour
scene won outright: it was the only one whose falls
pour broad and bright from the town's heart into the
bay, with real shadow modelling and no repeated
houses. The dusk and misty-morning candidates were
beautiful but weaker on the falls or off the concept.

## The audit (tile by tile, double zoom)

The full-resolution scene, 1120 by 2240, was cut into
six overlapping tiles and every tile was read at
double zoom: the two town arms, the falls source, the
falls middle and left cliff, the right cliff town,
and the lower harbour. Findings, worst first:

1. CRITICAL — the left cliff held a huge dark cave
   arch, and inside the arch a flat teal water surface
   floated at mid-cliff height beside the falls: a
   lake inside the rock, geometrically impossible,
   reading as a hole in the world.
2. CRITICAL — several small boats floated in the
   narrow river channel between the towns, right at
   the waterfall's lip, as if about to go over.
3. MAJOR — the falls poured out of a turquoise slot
   between buildings, with no visible river feeding
   them.
4. MAJOR — the smaller right-hand cascade emerged
   from underneath a cliff house, sourceless.
5. MINOR — a dark boat-shaped object floated in the
   plunge pool below the falls, reading as a wreck.
6. MINOR — one dinghy in the lower harbour was bright
   cyan-blue, a colour nothing else in the frame owns.
7. MINOR — a handful of window arches and balconies
   in the cliff houses were warped or uneven, and
   the distant cliff band behind the town sat flat.

The church, the castle, the sky and the harbour
layout were clean and were not touched in substance.

## The repairs

Each finding was repaired and then re-audited in the
same tiles before the next was accepted:

1. The cave and its floating water were painted out
   entirely; the left cliff is now solid sunlit rock
   with drifting mist, continuous with its neighbours.
2. Every boat was lifted out of the upper river. The
   channel now reads as clear flowing water running
   between the two towns to the lip.
3. The falls' crest was reworked over the cleared
   channel, so the water visibly pours from the river.
4. The right cascade now descends a stepped stream
   channel in a rock notch beside the houses; its
   source reads naturally.
5. The plunge-pool object became a dark rock outcrop
   ringed with white foam and spray.
6. The blue dinghy was repainted pixel-locally into
   weathered wood. Two first attempts at this micro
   fix failed visibly — one stained the water, one
   caught only part of the hull — and both were
   discarded; the accepted fix grew the boat's own
   connected shape and recoloured exactly that, so
   no trace of cyan and no smear remains.
7. Warped arches and balconies were straightened and
   the far cliff band softened into the haze.

The title was then composited once more, from the
repaired full-resolution scene: VEYRA in letterspaced
Noto Serif Display, ink a deep teal sampled from the
bay water, a thin rule with a centre diamond beneath,
placed in the calm sky clear of spire and castle.
The finished frame was downscaled to 512 by 1024.

## Re-audit result

All six zones were read again at double zoom after
the repairs: the cave is gone, the river is clear,
the cascades have sources, the harbour fleet shares
one palette, and the architecture reads deliberate.
No new artefact was introduced by any repair. The
only text in the frame is the name: V-E-Y-R-A.

## Verification of the shipped file

- `image.jpg`: JPEG, 512 × 1024, 175,685 bytes.
- sha256:
  `7fb905720262c8cfac5208370ff999429827010c8e1dbfe7258ed8484386009f`
- `main.py` run twice prints identical lines and the
  identical sha256 at `/output/entry.png`.
