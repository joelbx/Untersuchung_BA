Implemented `preview=true` for the direct, IA, and bulk MARC import endpoints. Preview runs return simulated keys, a `preview: true` flag, pending Edition, Work, and Author records in `edits`, and cover acceptability without saving records, uploading covers, or updating Archive.org metadata.

I also added case-insensitive cover host validation and the requested author and edition conversion interfaces. Validation and matching run through the same import pipeline in preview and normal modes.

Verification: **136 relevant tests passed**; Ruff and `git diff --check` passed.