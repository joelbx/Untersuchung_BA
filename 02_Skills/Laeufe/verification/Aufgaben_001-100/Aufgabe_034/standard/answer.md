Updated `get_ia_record` to split IA ISBNs into `isbn_10` and `isbn_13`, and publisher entries into `publishers` and `publish_places`. The new public utilities handle strings, lists, whitespace, and empty inputs. Added regression coverage.

Verification: 31 relevant tests passed; `git diff --check` passed. Ruff was unavailable locally (`ruff: command not found`), so lint status is unverified.