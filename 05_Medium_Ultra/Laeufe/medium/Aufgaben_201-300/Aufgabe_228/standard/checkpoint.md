Task: Replace specified version parsing and comparisons with Qt QVersionNumber.
Status: Implemented Qt-native parsing and comparisons in the requested modules.
Verification: 345 focused tests passed (qtutils, utils, distribution, crash dialog, earlyinit); git diff --check passed.
Note: The full test_version.py file exits with code 1 without a pytest summary during TestChromiumVersion::test_unpatched; its distribution tests passed in the focused run.
