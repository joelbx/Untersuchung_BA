Task: Implement URL hostname punycode conversion and apply it in useLinkHandler; notify on links without an extractable URL.
Status: Complete. Added getHostnameWithRegex and punycodeUrl in packages/components/helpers/url.ts; updated the hook and URL tests.
Verification: URL Jest suite 15/15 passed; components TypeScript check passed; targeted ESLint passed; Prettier check passed; git diff --check passed.
Delegation: None.
