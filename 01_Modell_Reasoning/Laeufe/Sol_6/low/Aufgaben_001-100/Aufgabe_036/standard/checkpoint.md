Task: fix config loader DB pool options and meta update-check handling.
Completed: added pool fields and conditional loading, made absent update-check false via Default(), loaded explicit update-check values, and updated config fixtures/tests.
Verification: go test ./config passed; git diff --check passed.
