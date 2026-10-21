---
itemId: SPEC-ALM-01
itemType: Software Item Spec
itemTitle: Alarm annunciation and silence
itemFulfills: KXITM7YSTXYQ0QE860ABFKKPB5NJT0A
---

## Item fields

### Description

Maps alarm kinds to priorities, enforces a minimum audio volume of 65 dBA for high-priority alarms, and caps any single silence action at 120 seconds.

Implemented in `src/aip/alarms.py`. Fulfills RQ-07.
