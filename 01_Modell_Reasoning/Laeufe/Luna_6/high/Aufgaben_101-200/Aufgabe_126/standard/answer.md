Implemented the assistant Markdown/HTML fixes. Message identity now flows through content preparation, editor insertion, and result rendering; URL restoration is scoped to that identity, and unrecognized links lose their URL while unrecognized images are removed.

Also preserved link and image class/style, enabled Markdown list conversion with configurable disabled rules, added `fixNestedLists`, and updated indentation cleanup to preserve nested list depth.

Validation: the existing assistant URL and composer content helper tests pass. Prettier and `git diff --check` pass. The mail workspace type check reports one unrelated OpenPGP type incompatibility in `packages/crypto/lib/worker/api.ts:579`.