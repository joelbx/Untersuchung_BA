# Checkpoint

Task: preserve formatting and message-scoped embedded links/images across assistant Markdown/HTML transformations.

Implemented:
- The composer message `localID` flows into model input preparation, rendered results, and editor insertion helpers.
- Link/image placeholders store their owning message ID and presentation attributes. Restoration only accepts the current message; unknown or cross-message links are unwrapped and images removed.
- HTML simplification retains `class` and `style` on links/images.
- Exported `fixNestedLists` repairs sibling nested lists. Markdown cleanup trims excess indentation while retaining nested list levels and code block contents.
- Assistant Markdown conversion enables list rules by default and supports custom disabled rules. Plain text conversion keeps its previous default disabled rules.

Verification:
- Assistant URL tests: pass (2 tests).
- Text-to-HTML regression tests: pass (4 tests).
- Targeted ESLint and Prettier checks passed before the final Markdown cleanup adjustment; the final helper check passed.
- Mail workspace type check reports the pre-existing OpenPGP type incompatibility at `packages/crypto/lib/worker/api.ts:579`; no changed Mail files were reported.
