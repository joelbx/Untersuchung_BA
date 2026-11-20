Fixed the shebang handling in [module_common.py](/app/lib/ansible/executor/module_common.py). New-style Python modules now use their declared interpreter and args by default; configured overrides still take precedence, and modules without a shebang use `/usr/bin/python`. The encoding line follows the shebang.

Added focused tests. The module-common suite passed: **56 tests**.