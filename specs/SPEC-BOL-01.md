---
itemId: SPEC-BOL-01
itemType: Software Item Spec
itemTitle: Patient bolus controller
itemFulfills: KXITM414TPW34K69PY98TKR3V5Y5YP5
---

## Item fields

### Description

Delivers the clinician-configured bolus volume when the patient presses the bolus key on the pump. A request inside the lockout interval is refused and logged. The bolus volume is checked against the drug library maximum when the controller is configured.

Implemented in `src/aip/bolus.py`. Fulfills RQ-05.
