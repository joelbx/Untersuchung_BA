Implemented Punycode conversion for URL hostnames while preserving the other URL components and removing a trailing path slash. External links now use the converted URL for navigation and confirmation; links whose URL cannot be extracted show an error notification.

Verification passed: 16 URL helper tests, the components TypeScript check, Prettier, and `git diff --check`.