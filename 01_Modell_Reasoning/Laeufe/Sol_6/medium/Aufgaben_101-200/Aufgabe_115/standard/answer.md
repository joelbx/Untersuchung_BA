MARC imports now map supported `$e` terms and `$4` codes to readable contributor roles, with `$4` taking precedence. New work entries preserve each role beside the correct author and raise an exception when edition and record author counts differ.

Updated the MARC fixtures and added parser, work, and import tests. **Verification:** 164 relevant tests passed; Ruff and `git diff --check` passed.