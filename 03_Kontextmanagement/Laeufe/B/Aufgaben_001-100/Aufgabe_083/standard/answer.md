Refactored the XAttr helpers to use `XAttrCreateParams`, added `DeepPartial` and explicit attribute types, and updated the upload call site. Creation now omits a zero block remainder and returns an immutable structure; parsing handles malformed or partial input without throwing.

The focused tests pass, the Drive TypeScript check passes with `--strict`, and `git diff --check` is clean.