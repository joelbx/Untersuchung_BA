# Checkpoint

Resolved assistant Markdown/HTML formatting and message-scoped URL handling in `/app`.

Implemented messageID propagation from composer identity into model preparation, editor insertion, result rendering, and URL restoration; added scoped link/image URL records and removal of unrecognized/cross-message media; retained class/style on links and images; enabled Markdown list parsing with customizable disabled rules; added exported `fixNestedLists`; and cleaned redundant indentation while preserving relative list depth.

Validation:
- Existing assistant URL and composer content helper tests pass.
- Prettier check and `git diff --check` pass.
- Mail workspace type check has only the existing unrelated OpenPGP type incompatibility in `packages/crypto/lib/worker/api.ts:579`.
