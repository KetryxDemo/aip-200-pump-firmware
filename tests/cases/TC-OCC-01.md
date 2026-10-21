---
itemId: TC-OCC-01
itemType: Test Case
itemTitle: Occlusion alarm within 2 minutes at 1, 25 and 500 mL/h
itemTests: SPEC-OCC-01
---

## Item fields

### Description

Verifies SPEC-OCC-01: occlusion alarm within 2 minutes at 1, 25 and 500 ml/h.

### Steps

Automated: `pytest tests/unit/test_occlusion.py::test_alarm_time`

### Expected behavior

All assertions pass.
