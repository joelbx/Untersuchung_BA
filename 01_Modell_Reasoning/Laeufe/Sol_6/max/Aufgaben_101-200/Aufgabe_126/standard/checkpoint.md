# Checkpoint

- Goal: Preserve assistant HTML formatting, list structure, and message scoped URLs through Markdown and HTML conversion.
- Repository: `/app`; working tree initially clean.
- Implemented: message scoped URL cache and restoration, retained link/image class and style, nested list repair, safe Markdown spacing, configurable disabled Markdown rules, and message ID propagation through composer, assistant, and insertion paths (including selected text replacement).
- Verified: focused assistant and composer tests (15), message content tests (4), ESLint, Prettier, and `git diff --check` pass.
- Type check: blocked by an existing OpenPGP type mismatch in `packages/crypto/lib/worker/api.ts:579` between top-level `openpgp` and `pmcrypto`'s nested `openpgp` types. No diagnostics were reported in edited files.
