# Checkpoint

Task: fix invalid `hosts` handling in `Play` using the assigned systematic-debugging process.

Initial repository search: `rg` is unavailable (`/bin/bash: rg: command not found`); continuing with local `grep`/`find`.

Status: investigating root cause; no repository code changes yet.

Investigation: `Play.load` derives `name` from `hosts` before `Base.load_data` and `Base.validate`, so invalid sequence members raise raw `TypeError`; an explicit name bypasses that code entirely. `Base.validate` already dispatches `_validate_<field>`, and `_ds` retains the input keys. Local sequence helper exists in `ansible.module_utils.common.collections` but is not exposed by `ansible.utils.collection_loader`; a reexport is needed to use the required path.

Hypothesis: remove name derivation from `Play.load`, use `get_name` for dynamic display, and validate only supplied `hosts` through the existing field validator hook. Baseline repro: `['none', {'test': 'x'}]` raises `TypeError: sequence item 1: expected str instance, dict found`. New focused tests fail on input mutation, tuple naming, and invalid hosts; command: `PYTHONPATH=lib:test python -m pytest -q test/units/playbook/test_play.py` (3 failed, 11 passed).

First patch check: 2 naming tests failed because `Base` defines `_name` with default `''`; `self.name is not None` treats this unset default as explicit. Direct inspection confirmed `p.name == ''`, `p.hosts == ['foo']`, and internal name attribute is `Sentinel`. Revised hypothesis: use the nonempty name value as the override, matching this class's default semantics.

Resolution: `Play.load` no longer derives or mutates `name`; `get_name` derives it from current hosts when no nonempty name is set. `_validate_hosts` uses `Base.validate` and checks only datasets containing `hosts`. The required `ansible.utils.collection_loader.is_sequence` path is supplied by reexporting the existing helper. Updated the existing integration assertion for the specified empty-host message.

Verification: `PYTHONPATH=lib:test python -m pytest -q test/units/playbook` passed (248 tests, 16 pre-existing deprecation warnings). `git diff --check` passed. A local `bin/ansible-playbook -i localhost, --syntax-check` invocation using the reported mixed hosts YAML exited 4 with `ERROR! Hosts list contains an invalid host value: '{'test': '^ this breaks things'}'` and a source location. The CLI integration shell suite was not run; only its expected message was updated.
