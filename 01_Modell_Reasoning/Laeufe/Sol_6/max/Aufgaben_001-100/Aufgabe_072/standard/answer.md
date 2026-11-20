Implemented hostname-only Punycode conversion and regex hostname extraction in [url.ts](/app/packages/components/helpers/url.ts). The [link handler](/app/packages/components/hooks/useLinkHandler.tsx) now uses punycoded external URLs and shows an error notification when it cannot extract a link URL.

Validation passed: 21 focused tests, component type check, targeted lint, and formatting check.