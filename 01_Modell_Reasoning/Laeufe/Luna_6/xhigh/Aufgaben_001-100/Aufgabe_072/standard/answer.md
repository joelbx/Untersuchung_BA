Implemented Punycode URL conversion and regex hostname extraction in [url.ts](/app/packages/components/helpers/url.ts). Updated [useLinkHandler.tsx](/app/packages/components/hooks/useLinkHandler.tsx) to normalize URLs before external link checks and show an error notification when it can’t extract a hostname.

The conversion preserves the protocol, path, query, and fragment while removing trailing path slashes.

Verified: URL helper tests passed (11 tests), TypeScript check passed, and components lint passed.