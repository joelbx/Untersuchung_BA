Implementer progress: inspecting module_common resolution and existing local tests; diagnosis is unverified.
Verified: collection lookup omits routing; package __init__ is stored under the wrong name and ancestor source is discarded. Implementing queued resolver with specialized locators.
Queued resolver and locators implemented; existing 8 resolver tests pass. Adding focused collection coverage and checking edge cases.
Completed queued dependency resolution, legacy/collection locators, routing shims, metadata handling, package source preservation and synthesis, and candidate-path errors. Added focused collection tests. Final local executor/module_common suite: 49 passed; git diff --check clean.
