Added `preview=true` to both import endpoints. Preview runs the import pipeline with UUID based temporary keys and returns `preview`, `edits`, and `cover_accepted` without saving records, uploading covers, or updating Archive.org metadata.

Author normalization and matching, language conversion, and case insensitive cover host validation now use the same logic in preview and regular imports. Preview reports cover acceptance; a cover ID is only available after an actual upload.

**Verification:** 165 relevant tests passed. Ruff and `git diff --check` passed.