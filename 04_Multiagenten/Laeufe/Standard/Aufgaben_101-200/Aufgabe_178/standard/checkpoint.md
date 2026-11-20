# Checkpoint

Implemented optional BCrypt `ident` through `password_hash`, both hash backends, and the password lookup. The lookup stores `ident` beside `salt` and reuses it on later runs; its default is `2a`. Added unit coverage and user guide example. Verified with `PYTHONPATH=lib python -m pytest -q test/units/utils/test_encrypt.py test/units/plugins/lookup/test_password.py test/units/plugins/filter/test_core.py` (60 passed).
