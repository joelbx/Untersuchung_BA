Implemented hostname-only Punycode conversion for external links. `punycodeUrl` preserves the URL’s other components and removes a trailing pathname slash; `getHostnameWithRegex` extracts the domain label. The link handler now shows an error notification when it cannot extract a usable URL.

Verification passed: 16 URL helper tests, the component type check, ESLint, and `git diff --check`.