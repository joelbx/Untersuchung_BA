# Checkpoint

Task: Fix pip module fallback when pip library is available without a pip executable.
Status: Inspecting repository and existing tests.
Verification: Pending.

Findings: `_get_pip` currently searches PATH and returns a string; `_get_packages` formats a shell command from it; main wraps pip in a one-element argv list and derives the virtualenv PATH prefix by string slicing. Existing unit coverage is in test/units/modules/test_pip.py.
Plan: detect pip via importlib.util.find_spec with pkgutil fallback, use current interpreter's `-m pip` launcher when appropriate, normalize all launcher forms to argv, and add focused tests.

Implementation: `_have_pip_module` uses importlib.util.find_spec with pkgutil.find_loader fallback and treats detection exceptions as unavailable. `_get_pip` returns argv and uses current interpreter `-m pip` when no executable or virtualenv is supplied. Package listing uses argv for list/freeze and returns a command string. Virtualenv PATH prefix uses os.path.join.
Verification history: Initial `python -m pytest -q test/units/modules/test_pip.py` failed because it imported an installed Ansible copy and the global fixture applied to unparametrized new tests. `PYTHONPATH=lib python -m pytest -q -o addopts='' test/units/modules/test_pip.py` then exposed a test assertion that counted Ansible's locale lookup; the test now isolates locale. Final focused run: 10 passed. `git diff --check`: exit 0.
