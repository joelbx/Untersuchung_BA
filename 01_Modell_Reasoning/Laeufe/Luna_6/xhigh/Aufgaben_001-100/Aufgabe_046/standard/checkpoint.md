# Work checkpoint

Issue: repair collection and legacy `module_utils` resolution in `lib/ansible/executor/module_common.py`.

Requirements being addressed: queue-based dependency traversal; specialized legacy/collection locators; redirects and redirect metadata; relative imports in package initializers; implicit package synthesis; deterministic missing-dependency diagnostics; base payload initializers; and `ansible.module_utils.six` normalization.

Initial status: repository inspected for agent instructions; none found in the working tree. Next: inspect implementation and existing tests, then implement and run relevant existing tests.

Findings: `recursive_finder` currently walks dependencies recursively, collection lookup does not process collection routing, and collection package initializer imports are not reliably carried through. `ModuleDepFinder` stores import targets without preserving ambiguity context. The payload wrapper already seeds `ansible/__init__.py` and `ansible/module_utils/__init__.py`; that behavior will remain explicit.

Implementation in progress: replacing the resolver internals with specialized locators and a work queue while keeping the public function signature.

Implementation complete: `ModuleDepFinder` preserves ambiguous from-imports and resolves relative names against the containing package; dedicated legacy and collection locator classes handle local/redirect priority, routing metadata, FQCN expansion, shims, tombstones, and deprecation warnings. `recursive_finder` now drains a queue, adds base `basic` support, normalizes all six imports, synthesizes collection and namespace package initializers, and reports attempted FQNs for unresolved imports.

Validation: `python -m py_compile lib/ansible/executor/module_common.py`; focused existing unit tests passed (46 tests); `git diff --check` passed. Also exercised actual collection fixture payload assembly for nested implicit packages, package initializer relative imports (including a cousin package), and a cross-collection module_utils redirect.
