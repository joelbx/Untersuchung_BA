# Checkpoint

Task: Add encoding validation to FormatString and enforce ASCII for the user-agent configuration.

Changes: `FormatString` accepts an optional encoding, validates during `to_py`, and includes it in its representation. `content.headers.user_agent` specifies ASCII. Added type and configuration tests for ASCII rejection, other encodings, and unrestricted backward compatibility.

Verification: `python -m pytest -q tests/unit/config/test_configtypes.py tests/unit/config/test_configdata.py` passed (1140 passed, 10 xfailed). `git diff --check` passed.

Tooling: `rg` was unavailable (`/bin/bash: rg: command not found`); local grep was used for inspection.
