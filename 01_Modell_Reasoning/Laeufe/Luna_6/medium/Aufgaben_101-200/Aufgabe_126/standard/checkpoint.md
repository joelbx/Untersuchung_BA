# Checkpoint

Implemented message-scoped URL placeholders and propagation through preparation, rendering, and editor insertion; preserved class/style on links and images; enabled Markdown lists with configurable disabled rules; added `fixNestedLists`; and corrected whitespace cleanup to retain list hierarchy indentation.

Verification: existing `url.test.ts` passes. `git diff --check` passes. `yarn workspace proton-mail check-types` reports one pre-existing dependency type error in `packages/crypto/lib/worker/api.ts:579` involving incompatible OpenPGP types; no errors reported in the changed files.
