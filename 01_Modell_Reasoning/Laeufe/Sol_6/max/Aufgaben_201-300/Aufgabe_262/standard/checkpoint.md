# Checkpoint

Resolved cover URL filtering in openlibrary/catalog/add_book/__init__.py. Added ALLOWED_COVER_HOSTS and public process_cover_url helper; both new/overwritten and matched-edition imports validate HTTP(S) hosts before add_cover, and remove cover from the edition/record dictionary. Added unit and import regression coverage in test_add_book.py. Verification: full add_book suite 151 passed, 1 xfailed; focused cover tests 12 passed; Ruff and git diff --check passed.
