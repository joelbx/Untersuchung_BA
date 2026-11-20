Implemented IDN URL handling. External links now have their hostnames converted to Punycode before confirmation or navigation, while their paths, queries, and fragments stay intact. Links without an extractable URL show an error notification, and the confirmation modal recognizes Punycode in subdomains.

Verification passed: 17 targeted tests, TypeScript, ESLint, Prettier, and `git diff --check`.