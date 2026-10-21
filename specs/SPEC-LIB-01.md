---
itemId: SPEC-LIB-01
itemType: Software Item Spec
itemTitle: Drug library limit checks
itemFulfills: KXITM1FT62GZNAM83YRBMQT3FW60EDB
---

## Item fields

### Description

Holds one entry per drug (concentration, soft and hard maximum rate in mL/h, maximum bolus in mL). `check_rate` returns OK, SOFT (clinician must confirm) or HARD (rejected, no override) for every programmed rate.

Implemented in `src/aip/drug_library.py`. Fulfills RQ-04.
