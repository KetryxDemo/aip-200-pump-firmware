---
itemId: SPEC-PUMP-01
itemType: Software Item Spec
itemTitle: Delivery interlock and cassette latch
itemFulfills: KXITM614MZJCG6V95KT0BCX9CQ5YEQP
---

## Item fields

### Description

Motor start is permitted only when the cassette latch sensor reports CLOSED. Opening the latch during delivery stops the motor within one control cycle and engages the anti-free-flow clamp.

Implemented in `src/aip/pump.py`. Fulfills RQ-02.
