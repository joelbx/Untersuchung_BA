Task: Fix book import cover handling for unsupported hosts.
Status: Complete.
Changes: Added ALLOWED_COVER_HOSTS and process_cover_url; applied validation to new and matched edition import paths; added coverage for allowed/unsupported and malformed URLs.
Verification: 88 add_book tests passed; Ruff checks passed; git diff --check passed.
Constraints: Local repository code and tests only; no git history, index baseline, or harness configuration changes.
