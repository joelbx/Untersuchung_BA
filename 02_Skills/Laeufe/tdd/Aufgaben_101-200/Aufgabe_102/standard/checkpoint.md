# Checkpoint

Task: Add Linux scope-host locally reachable IP facts with IPv4 and IPv6 lists.

Status: Implemented `locally_reachable_ips` on Linux with IPv4/IPv6 lists from local routes. Normalizes, deduplicates, sorts, and returns empty lists with warnings on unavailable route queries.

TDD: Four new tests failed for missing method/fact before implementation, then passed afterward.

Checks:
- `python -m pytest -q test/units/module_utils/facts/network/test_linux_locally_reachable.py`: 4 passed.
- `python -m pytest -q test/units/module_utils/facts/network test/units/module_utils/facts/test_facts.py`: 100 passed, 5 skipped.
- `python -m pytest -q test/units/module_utils/facts`: 398 passed, 7 skipped, 1 failed (`test/units/module_utils/facts/test_timeout.py::test_implicit_file_default_timesout`, expected timeout but returned `Succeeded after 2 sec`), 42 warnings.
- `python -m pytest -q`: interrupted after unrelated collection and CLI failures; at interruption 13 failed, 92 passed, 49 errors. Examples: `test/ansible_test/unit/test_diff.py` import error (`to_text` unavailable), `test/units/cli/test_adhoc.py::test_with_command` (`KeyError: module_name`), and `test/units/cli/test_galaxy.py::TestGalaxy::test_display_galaxy_info` (TypeError). Full suite result remains uncertain because run was interrupted.

Environment: `ip` executable is absent, so live kernel route output could not be checked locally; tests use representative `ip route` output.

`git diff --check` passed.
