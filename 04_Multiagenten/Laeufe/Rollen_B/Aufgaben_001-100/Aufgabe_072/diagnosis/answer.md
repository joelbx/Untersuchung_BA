I located the failure but did not edit project source or tests: this task assigns me a fault-localization-only role.

- [url.ts](/app/packages/components/helpers/url.ts:12) has neither requested function. The example `www.abc.com → abc` suggests `getHostnameWithRegex` should return a domain label, but the requirement does not define how to handle multi-part suffixes.
- [useLinkHandler.tsx](/app/packages/components/hooks/useLinkHandler.tsx:85) applies punycode to URL path segments as well as the hostname. A local reproduction changed Unicode path and query text. Conversion also runs only when a confirmation modal opens.
- [useLinkHandler.tsx](/app/packages/components/hooks/useLinkHandler.tsx:49) silently turns a missing `href` into an empty string; the error notification runs only if extraction throws.
- [LinkConfirmationModal.tsx](/app/packages/components/components/notifications/LinkConfirmationModal.tsx:32) recognizes `xn--` only immediately after `://`, so it misses `www.xn--…`.

The fix should encode hostname labels only, preserve the other URL components without adding a trailing slash, normalize external links before processing, and notify on an unextractable URL. The existing [URL tests](/app/packages/components/helpers/url.test.ts) do not cover these behaviors. I recorded the diagnosis in [checkpoint.md](/app/.codex-role-output/checkpoint.md).