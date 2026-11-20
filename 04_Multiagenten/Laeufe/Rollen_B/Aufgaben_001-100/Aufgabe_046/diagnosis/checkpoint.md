# Fault localization checkpoint

Inspected `lib/ansible/executor/module_common.py`, collection loader metadata support, and existing unit/integration fixtures. Ran `PYTHONPATH=lib python -m pytest -q test/units/executor/module_common/test_recursive_finder.py`: 8 passed.

Likely fault sites:
- `CollectionModuleInfo.__init__` (~657-687) has explicit module_utils redirect TODO and never checks `plugin_routing.module_utils`; `recursive_finder` (~720-944) only uses `InternalRedirectModuleInfo` for legacy names after local failure. Cross-collection redirects are absent from payload.
- `CollectionModuleInfo` does not set `pkg_dir` when `__init__.py` is found; `recursive_finder` (~822-848) writes package source as `<package>.py`, replaces ancestor package initializers with empty strings, and scans the wrong FQN. Package-relative imports in real collection `__init__.py` are therefore lost.
- `ModuleDepFinder.visit_ImportFrom` (~515-534) calculates relative names by slicing `module_fqn` by `node.level`; package source needs an explicit package context. Existing legacy names append `__init__`, but collection package names do not.
- `recursive_finder` (~772-813) tries last one/two components indiscriminately, even for shallow module_utils paths. Missing dependency error (~810-817) reports leaf names and originating short name, not full candidate FQNs.
- `recursive_finder` (~886-906) loads all legacy ancestor `__init__.py` files without a missing-file fallback; collection branch (~832-848) always creates empty ancestors and does not preserve real inits. Base ansible inits are seeded at ~1126-1144 only in payload assembly.
- `_get_collection_metadata` in `_collection_finder.py` (~955) already raises `ValueError('unable to locate collection ...')`; resolver should propagate/contextualize that exact condition for redirect targets. `display.deprecated` in display.py (~382) supports warning text, version, date, collection_name and removed errors.

Recommended fix behavior: queue work items carrying source, FQN and package status; specialized local-first legacy and redirect-first collection locators with attempted full names; normalize six; read and scan actual package initializers, synthesize only absent ones; turn every routing redirect into a shim and enqueue its expanded FQCN target; handle deprecation and tombstone metadata while processing; retain base package files. Existing integration runtime fixture has a cross-collection module_utils redirect at `test/integration/targets/collections/collection_root_user/ansible_collections/testns/testcoll/meta/runtime.yml`.

Uncertainty: no dedicated unit cases here for collection module_utils package initializers, missing nested inits, redirect deprecation/tombstones, or missing target collections; root cause is code-path evidence rather than a reproduced playbook failure.
