# Import preview implementation checkpoint

Task: add non-persistent preview support to import endpoints, expose prospective Edition/Work/Author edits, and align cover, author, and language validation across preview and normal imports.

Status: complete. The import pipeline accepts `save=False`, returns UUID based temporary keys and prospective edits, validates cover hosts, and skips persistence, cover uploads, and Archive.org updates. Both import endpoints forward `preview=true`. Author normalization, matching, and remote ID merging are shared by preview and regular imports. Verification: 165 relevant tests passed; Ruff and `git diff --check` passed.
