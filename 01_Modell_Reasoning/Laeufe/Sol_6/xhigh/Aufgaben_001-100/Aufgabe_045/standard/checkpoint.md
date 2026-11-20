Issue: collection names containing Python keywords are accepted.

Implemented: AnsibleCollectionRef now validates each matched name segment as a Python identifier and rejects Python keywords. Dependency resolution uses this shared validator; its legacy FQCN and Python 2/3 helper code was removed. Untyped collection-reference validation also checks the collection prefix. Added focused regression tests.

Verification: collection loader (81 passed), Galaxy collection install (32 passed), and Galaxy collection (43 passed). The first two suites were rerun after the final validator edit and passed. Galaxy tests require a collection finder installed before invoking pytest; plain pytest lacks that setup. `git diff --check` passed.
