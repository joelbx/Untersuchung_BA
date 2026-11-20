Implemented multi-device U2F challenges in [auth.go](/app/lib/auth/auth.go). The payload keeps the first challenge in the legacy JSON fields and adds `challenges` for every registered token. The CLI now accepts either format and can sign with any listed token. The web API returns the enhanced payload, and MFA management is hidden from CLI help.

The JSON compatibility test, existing U2F web login test, and new second-token login test pass. The client and `tsh` packages compile.

**Remaining limit:** the bundled browser UI still submits only the legacy first challenge. Its source is outside this repository, so browser token choice remains unfinished.