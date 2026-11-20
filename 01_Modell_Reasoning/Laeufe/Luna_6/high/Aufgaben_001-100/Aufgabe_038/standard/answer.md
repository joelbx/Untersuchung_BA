Implemented transparent gzip decoding in the shared URL utilities and passed the `decompress` option through `uri` and `get_url`. Requests now advertise gzip by default; `decompress=False` preserves the compressed response. Added regression coverage for both behaviors.

Validation: `python -m pytest -q test/units/module_utils/urls` passed (81 tests), `compileall` passed, and `git diff --check` passed.

Key files: [urls.py](/app/lib/ansible/module_utils/urls.py), [uri.py](/app/lib/ansible/modules/uri.py), [get_url.py](/app/lib/ansible/modules/get_url.py).