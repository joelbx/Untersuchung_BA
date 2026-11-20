# Checkpoint

Task: Implement safe Punycode URL handling and improve URL extraction/error reporting in the link handler.

Completed:
- Added `getHostnameWithRegex` and `punycodeUrl` in `packages/components/helpers/url.ts`.
- Updated `useLinkHandler` to normalize URLs before hostname/external-link checks and notify when a URL cannot be extracted.
- Preserved pathname, query, and fragment text while removing trailing pathname slashes.

Validation passed:
- Existing URL helper tests: 11 passed.
- Components TypeScript check.
- Components lint.
- `git diff --check`.
