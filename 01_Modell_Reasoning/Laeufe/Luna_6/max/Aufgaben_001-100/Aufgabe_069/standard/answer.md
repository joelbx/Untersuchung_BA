Implemented matcher parsing in [parse.go](/app/lib/utils/parse/parse.go:34): literal, wildcard, and regexp matchers; `regexp.match`, `regexp.not_match`, and `email.local`; static prefix/suffix matching; and the required validation errors. `Variable()` now rejects regexp matcher calls.

`go test ./lib/utils/parse` passed. The checkpoint is recorded in `.codex-role-output/checkpoint.md`.