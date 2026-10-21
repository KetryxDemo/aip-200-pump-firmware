---
itemId: TC-OCC-02
itemType: Test Case
itemTitle: No alarm on short pressure transients
itemTests: SPEC-OCC-01
---

## Item fields

### Description

Verifies SPEC-OCC-01: no alarm on short pressure transients.

### Steps

Automated: `pytest tests/unit/test_occlusion.py::test_transient_rejected`

### Expected behavior

All assertions pass.
