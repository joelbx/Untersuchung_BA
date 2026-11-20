Task: Simplify useMyCountry to return a country string or undefined; update listed consumers and PhoneInput default-country initialization.
Status: Implementation complete and reviewed.
Changes: Hook returns country only. Seven consumers use the single value; user settings gates remain. PhoneInput starts empty for missing/empty defaults, adopts the first non-empty default after mount only when its country state is empty, and ignores later default changes. Focused PhoneInput tests cover these transitions.
Validation: PhoneInput and useMyCountry suites pass (18 tests). Prettier check and git diff --check pass. Components and account type checks both stop on the same unrelated openpgp/pmcrypto type mismatch in packages/crypto/lib/worker/api.ts:579; neither reports diagnostics in edited files.
Constraints followed: Local code and tests only; no git history, index baseline, or harness configuration changes.
