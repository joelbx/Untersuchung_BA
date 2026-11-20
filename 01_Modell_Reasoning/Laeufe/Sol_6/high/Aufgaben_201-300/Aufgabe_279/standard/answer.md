Payment token creation now accepts an injectable verifier. The default verifier owns the verification modal and timer based polling, and all payment callers—including the additional single signup caller—use the new factory functions.

The relevant payment and signup tests pass, both component and account type checks pass, and `git diff --check` is clean.