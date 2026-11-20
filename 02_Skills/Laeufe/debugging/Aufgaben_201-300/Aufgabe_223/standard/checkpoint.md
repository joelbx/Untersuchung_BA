# Checkpoint

Task: Resolve module shebang handling for Python and other interpreters.

Status: Investigating root cause. `rg` is unavailable in this environment; using local `find` and `grep` for repository inspection.

Root cause: `_find_module_utils` calls `_get_shebang('/usr/bin/python', ...)` for every new-style Python module (line 1244), losing the source shebang before creating the wrapper. `_get_shebang` can return `None` as its shebang and `modify_module` has no shared extractor, so preservation depends on a separate old-style path. The default `INTERPRETER_PYTHON` is `auto`; an explicit configured path must still take precedence.

Hypothesis: Extracting the source interpreter before wrapping, then resolving explicit overrides against that interpreter, will preserve author shebangs and args. A missing source shebang can fall back to `/usr/bin/python`.

Implemented: `_extract_interpreter` parses the source shebang with `shlex.split`. `_get_shebang` always returns a complete shebang and resolved interpreter. New-style Python wrappers use the source interpreter and preserve the original shebang text when no override changes it. Old-style modules replace the shebang only when the interpreter changes, preserving literal argument text; both paths put the encoding comment after a shebang. Explicit Python configuration and inventory overrides retain precedence, including explicit `auto` discovery.

Verification: Before the fix, the focused regression run failed in seven expected cases (missing extractor, missing returned shebang, and new-style discovery before source extraction). After the fix, `python -m pytest -q test/units/executor/module_common` passed: 60 tests. `git diff --check` passed. The test run emitted an existing `ZipFile.__del__` warning from `test_recursive_finder`; no test failed.
