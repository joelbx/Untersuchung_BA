Implemented undefined handling in [dumper.py](/app/lib/ansible/parsing/yaml/dumper.py:44): the representer triggers Jinja’s undefined error, which Templar converts to `AnsibleUndefinedVariable`.

Both filters in [core.py](/app/lib/ansible/plugins/filter/core.py:48) now let undefined errors reach Templar and wrap other dump failures in filter-specific `AnsibleFilterError`s, retaining the original exception in `orig_exc`.

Verification: 11 existing unit tests passed. Manual checks confirmed undefined values fail through Templar, other dump errors preserve their cause, and supported mappings still round-trip. `git diff --check` is clean.