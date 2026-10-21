---
itemId: SPEC-PWR-01
itemType: Software Item Spec
itemTitle: Battery run-time and power alarms
itemFulfills: KXITM38RQYJBPYZ9YV8AQFZ6ARP3W5D
---

## Item fields

### Description

Estimates remaining run time from battery capacity and present current draw. Raises a medium-priority low-battery alarm at 30 minutes and a high-priority depleted alarm at 5 minutes remaining.

Implemented in `src/aip/power.py`. Fulfills RQ-06.
