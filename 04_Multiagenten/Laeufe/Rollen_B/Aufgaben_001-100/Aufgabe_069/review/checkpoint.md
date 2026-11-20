VERDICT: FIX

Reviewed the applied matcher patch. `go test ./lib/utils/parse` passed (`ok`, 0.004s); `git diff --check` passed. Code defects remain:

- `Variable(`{{regexp.match("^a{2}$")}}`)` is rejected by `reVariable` before matcher detection because the regex excludes braces inside the quoted argument. It returns the generic template bracket error instead of the required exact matcher-function error. Fix by identifying matcher calls even when their quoted regexp contains braces.
- `Match(`{{regexp.match("}}")`)` has no closing outer `}}`, but `LastIndex("}}")` finds the token inside the string literal; the parse failure returns the generic invalid matcher error instead of the required malformed-template error. Fix by finding template delimiters outside quoted arguments and validating the closing delimiter.
