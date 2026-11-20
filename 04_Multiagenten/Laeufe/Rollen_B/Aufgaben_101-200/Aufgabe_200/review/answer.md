VERDICT: FIX

**Code review:** I found no confirmed defect in the duration parser or its `:later` integration. I made no project code changes.

**Tests run:**

- `pytest -q tests/unit/utils/test_utils.py -k parse_duration` — 23 passed, exit 0.
- `pytest -q tests/unit/misc/test_utilcmds.py -k later` — 6 passed, exit 0.
- `QTWEBENGINE_DISABLE_SANDBOX=1 pytest -q tests/end2end/features/test_utilcmds_bdd.py -k later --qute-bdd-webengine --reruns 0 --tb=short` — 4 passed, 1 expected failure, exit 0.
- `pytest -q tests/unit/utils/test_utils.py` — 184 passed, exit 0.
- `pytest -q tests/unit/misc/test_utilcmds.py` — all 9 tests reported passed, but the process exited 1 after an X11 connection error. A sequential retry had the same result.

**TEST_ENVIRONMENT_PROBLEM:** The full command unit suite lacks a successful exit. Rerun it with a stable Xvfb display and require exit 0 before accepting the patch. Earlier end to end startup failures were due to unavailable QtWebKit and QtWebEngine’s root sandbox restriction; the command above ran those scenarios successfully.

The full command history and evidence are in [checkpoint.md](/app/.codex-role-output/checkpoint.md).