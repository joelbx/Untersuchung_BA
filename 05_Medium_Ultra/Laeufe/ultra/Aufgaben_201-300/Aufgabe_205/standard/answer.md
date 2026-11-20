Implemented the token lifecycle interface in [src/api/utils.js](/app/src/api/utils.js): generation, ordered listing, single and batch retrieval, description updates, deletion, usage logging, and last-seen lookup. Bearer authentication now accepts tokens created through that interface, while existing settings-based tokens remain supported.

Delegated repository and database review, plus the lifecycle test draft; I integrated and verified the patch. The lifecycle and authentication suites pass together (**50 tests**). ESLint and `git diff --check` pass.

Existing admin and public token management still uses `core.api` settings; this patch does not migrate those legacy tokens into the new indexes.