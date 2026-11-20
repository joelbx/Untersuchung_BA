Task: Add explicit override-validation support to import API and add is_promise_item utility.
Status: Complete.
Changes: POST reads override-validation from URL query and forwards the boolean to load and validate_record. Required fields remain enforced; publication year, independent publisher, and source ISBN checks are skipped only on explicit override. Added case-insensitive promise source detection.
Verification: 116 selected tests passed across add_book, import API, and catalog utils. Ruff passed with pre-existing UP035 import warning ignored; git diff --check passed.
