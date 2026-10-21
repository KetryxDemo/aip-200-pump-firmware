---
itemId: SPEC-OCC-01
itemType: Software Item Spec
itemTitle: Occlusion detector
itemFulfills: KXITM1FMMAHD7KR9T6A7V28CG21DY8N
---

## Item fields

### Description

Samples downstream line pressure at 1 Hz, applies a moving-average filter over `FILTER_WINDOW` (5) samples, and compares the result to a rate-scaled threshold (40 kPa + 0.12 kPa per mL/h). The occlusion alarm fires only after the filtered pressure stays above threshold for `PERSISTENCE_S` (10) seconds, which rejects transients from patient movement.

Design constraint: worst-case time to alarm must stay under 2 minutes at 1 mL/h.

Implemented in `src/aip/occlusion.py`. Fulfills RQ-01.
