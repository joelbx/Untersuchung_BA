# Checkpoint

Task: simplify useMyCountry to return country or undefined; update listed consumers; adjust PhoneInput default-country initialization and one-time adoption.

Status: implemented. No delegation used.

Verification: PhoneInput and useMyCountry Jest suites passed (17 tests). Prettier check passed on changed core files. Components type check failed in unchanged packages/crypto/lib/worker/api.ts because openpgp and pmcrypto's openpgp types differ.
