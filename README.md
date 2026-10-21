# AIP-200 Ambulatory Infusion Pump - control software

Hypothetical demo product. Requirements and DFMEAs live in Ketryx; this repo
holds the code, the software item specs (`specs/`) and the test cases
(`tests/cases/`, automated in `tests/unit/`).

Every pull request opens a Change Request in Ketryx (`.github/workflows/pr-to-dfmea.yml`).
The Ketryx "PR to DFMEA" agent reads it and says whether an existing DFMEA
already covers the change, which DFMEA row needs its scope broadened, or that
a new DFMEA is needed.
