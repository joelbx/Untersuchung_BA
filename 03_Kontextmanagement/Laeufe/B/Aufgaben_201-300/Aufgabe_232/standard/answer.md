Implemented OS EOL lookup and scan warnings. The summary now prints each warning with the required `Warning: ` prefix and preserves its order. OS family identifiers and major version parsing are centralized, and Amazon Linux 1 and 2 releases are handled separately.

Relevant Go tests passed for `config`, `util`, `scan`, `oval`, `gost`, and `report`; `git diff --check` passed.