# Checkpoint

Task: Fix RPM installed package parsing for non-standard source RPM filenames and epochs.

Plan: Inspect scanner RPM parsing and nearby tests; make malformed SOURCERPM values warnings while retaining binary metadata; parse epochs from source RPM filenames while preserving binary/source linkage; run relevant existing tests.
