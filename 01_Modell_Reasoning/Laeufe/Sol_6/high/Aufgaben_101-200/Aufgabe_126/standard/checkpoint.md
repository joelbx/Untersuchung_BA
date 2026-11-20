# Checkpoint

Completed message-scoped assistant URL placeholders and restoration, link/image attribute preservation, nested-list normalization, Markdown list conversion, code block line-break preservation, and composer messageID propagation. Added regression tests for cross-message URLs, round-trip formatting, lists, and code blocks. Relevant tests pass (14/14), focused ESLint passes, and git diff --check passes. Repository type check remains blocked by a pre-existing OpenPGP type conflict in packages/crypto/lib/worker/api.ts.
