# Checkpoint

Implemented `widened_hostnames` in `qutebrowser/utils/urlutils.py` with the specified empty, single-label, multi-label, and edge-string behavior.

Updated `HostBlocker._is_blocked` to check the enabled toggle and whitelist before matching each request-host parent against runtime and config block sets. Trailing root dots are treated equivalently in requests and blocklist entries.

Added regression tests for widening, parent-domain blocking through both sets, full URLs, trailing dots, whitelist precedence, and per-URL disabling through a parent-domain block. Updated the existing per-URL test to use a full URL because a scheme-less `QUrl` has no host.

Verification: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/components/test_hostblock.py tests/unit/utils/test_urlutils.py` passed (357 passed, 1 skipped). After the final per-URL test adjustment, `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/components/test_hostblock.py::test_disabled_blocking_per_url` passed (1 passed). `git diff --check` passed before that final test-only adjustment.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); local `grep` and `find` were used instead. An initial full test run had one failure in the pre-existing per-URL test due to its scheme-less URL; this was corrected and the suite passed.
