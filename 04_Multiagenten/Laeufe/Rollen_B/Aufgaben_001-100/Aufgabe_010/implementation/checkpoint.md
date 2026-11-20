Verified: tombstone notice is a span plus br; reply and search cancel controls are icon-only and unlabeled. DisambiguatedProfile has a fixed div root. Implementing semantic paragraphs, an inline profile option for reply header, and a shared labeled cancel control for reply/search.

Composer and search tests passed. Typecheck found a size prop collision with AccessibleButton's inherited HTML input size attribute; adjusting the shared button prop type. Other current type errors are in SDK/room settings files outside this patch.

Implemented and verified: tombstone status/link are paragraphs; reply header names the sender through an inline DisambiguatedProfile; reply/search use a labeled shared CancelButton with configurable size. Four relevant Jest suites (10 tests), targeted ESLint, stylelint, and git diff --check pass. Full TypeScript check remains blocked by five existing errors in matrix-js-sdk and room settings; none point to edited files.
