# Checkpoint

Issue: parent-domain host blocking, whitelist precedence, and hostname widening.
Plan: inspect local code/tests, add failing regression tests, implement minimal fix, run targeted and project tests.
Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using `grep`/`find`.

Implemented `urlutils.widened_hostnames` and parent-domain host blocking with early whitelist override. Added regression tests for widening, both block sets, full URLs, trailing dots, and whitelist precedence. Updated an existing per-URL test fixture to use a full URL instead of an empty-host relative QUrl.
RED observed: 15 failing new cases (missing helper and unmatched subdomains). GREEN targeted: 19 passed. Affected files: 435 passed, 1 skipped (`QT_QPA_PLATFORM=offscreen pytest -q -o addopts='' tests/unit/components/test_hostblock.py tests/unit/utils/test_urlutils.py tests/unit/config/test_configutils.py --benchmark-disable --tb=short`).
Project suite command running: `timeout 120s env QT_QPA_PLATFORM=offscreen pytest -q -o addopts='' --tb=short`.

Project suite limitation: end-to-end tests fail at startup. Reproduced with `timeout 20s env QT_QPA_PLATFORM=offscreen pytest -q -x -o addopts='' --tb=short tests/end2end/features/test_open_bdd.py`: `tests/end2end/features/test_open_bdd.py::test_open_s[http://]` errors with `ProcessExited`; startup log says QtWebKit could not be imported (`cannot import name 'QtWebKit' from 'PyQt5'`). The full suite command has the same early errors; final exit status pending.

Optional style check unavailable: `flake8 qutebrowser/components/hostblock.py qutebrowser/utils/urlutils.py tests/unit/components/test_hostblock.py tests/unit/utils/test_urlutils.py` -> `/bin/bash: flake8: command not found` (exit 127). Style lint remains unverified; `git diff --check` passed.

Final project suite outcome: `timeout 120s env QT_QPA_PLATFORM=offscreen pytest -q -o addopts='' --tb=short` exited 124 after 120 seconds. It collected 9,523 items (7 skipped), reported repeated end-to-end startup errors caused by missing QtWebKit, and stalled while running `tests/end2end/fixtures/test_webserver.py`. The full suite is therefore unverified. No dependencies were downloaded.
