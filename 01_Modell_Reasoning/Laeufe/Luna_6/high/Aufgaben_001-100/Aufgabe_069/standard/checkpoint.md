# Checkpoint

Implemented matcher support in `lib/utils/parse/parse.go`:

- Added the public `Matcher` interface and `Match` parser.
- Added regexp, negation, prefix/suffix, and email local-part matcher implementations.
- Added literal/wildcard conversion through `utils.GlobToRegexp`, anchored generated patterns, and support for raw anchored regexps.
- Added validation for matcher function namespaces, names, argument count/type, malformed templates, and matcher function use in `Variable()`.
- Preserved static template prefix/suffix text exactly.

Verification: `go test ./lib/utils/parse` and `git diff --check` pass.
