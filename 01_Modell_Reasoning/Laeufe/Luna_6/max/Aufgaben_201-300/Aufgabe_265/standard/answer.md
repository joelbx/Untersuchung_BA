Updated [QtColor](/app/qutebrowser/config/configtypes.py:1004) to scale hue percentages to 0–359 and other percentages to 0–255. It now checks function names and component counts before parsing, then uses the matching `QColor` constructor.

Updated [QtColor tests](/app/tests/unit/config/test_configtypes.py:1241) to cover percentage inputs for all four formats and invalid HSV/HSVA forms.

**Verification:** The focused test class passed: 32 tests. The full module run reported broad Hypothesis and Qt/PyQt compatibility failures; it also caught two endpoint cases that were fixed before the final focused run. `git diff --check` passed.