# Checkpoint

Task: Add import API override-validation and promise item utility.
Status: Complete.
Changes: URL query flag forwarded through importapi.POST -> add_book.load -> validate_record; optional checks bypassed only when true; is_promise_item added.
Verification: 112 targeted tests passed; git diff --check passed. Ruff reports pre-existing UP035 in catalog/utils import.
