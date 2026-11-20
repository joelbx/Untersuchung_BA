Task: replace expression parsing and matcher logic in lib/utils/parse with a typed AST, update trait and PAM callers, and run existing tests.
Implemented AST nodes, predicate-backed parsing, matcher AST, trait and PAM validation, and behavior-based parser and service tests.
Verification: parser tests and focused services tests pass offline; git diff --check passes. lib/srv test build is blocked by missing local C headers and sqlite symbols (and CGO-disabled dependencies do not compile).
