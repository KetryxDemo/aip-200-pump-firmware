---
itemId: SPEC-DOSE-01
itemType: Software Item Spec
itemTitle: Dose-to-rate conversion
itemFulfills: KXITM53EQQNH2YS9AH9AP39SAB7WE6E
---

## Item fields

### Description

Converts a programmed dose into a delivery rate in mL/h. Supported dosing modes are `ml_h` (volume) and `mg_h` (mass, divided by the drug library concentration in mg/mL). Any other mode is rejected. The computed mL/h rate is always returned with `needs_confirmation: true` so the UI shows it to the clinician before delivery starts.

Implemented in `src/aip/dosing.py`. Fulfills RQ-03.
