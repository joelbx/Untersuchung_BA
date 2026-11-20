# Checkpoint

Task: preserve HTML formatting and scope assistant links/images by messageID.
Status: implementation complete in checked-out files; focused assistant tests pass (6 tests). TypeScript check reports an unrelated existing OpenPGP type mismatch in packages/crypto/lib/worker/api.ts. Targeted lint and diff check pass.
Changes: propagated composer identity through model preparation, preview, and insertion; scoped URL maps and restoration; retained link/image class and style; repaired nested lists; enabled list rendering in assistant Markdown and exposed configurable disabled rules.
