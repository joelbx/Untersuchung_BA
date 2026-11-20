Book imports now remove every `cover` field before saving the edition and upload the image only when its HTTP or HTTPS hostname matches `ALLOWED_COVER_HOSTS`, case-insensitively. The new `process_cover_url` callable handles missing, unsupported, and valid covers in both new and matched edition imports.

Verification: 89 add-book tests passed; Ruff and `git diff --check` passed.