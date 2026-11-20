# Checkpoint

Task: implement matcher expressions in `lib/utils/parse`.

Completed:
- Added the `Matcher` interface and regexp, prefix/suffix, negation, and email local-part matcher implementations.
- Added `Match` parsing for literal and wildcard patterns, anchored raw regexps, and supported `regexp.match`, `regexp.not_match`, and `email.local` calls.
- Added validation for template delimiters, matcher expression shape, namespaces, functions, and string literal arguments. `Variable()` now rejects regexp matcher calls with the required error.
- Preserved static prefix and suffix text around a single matcher template.

Verification: `go test ./lib/utils/parse` passed.
