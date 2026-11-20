Added a dedicated `VulnInfo.KEVs` field with CISA and VulnCheck details. `FillWithKEVuln` now populates it from both sources, including VulnCheck exploit records, and normalizes invalid due dates. Added the KEV summary and stable JSON ordering.

The repository tests for `models` and `detector` passed, as did the focused KEV tests and `git diff --check`.