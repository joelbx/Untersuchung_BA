I located the fault, but did not edit project source or tests: this run was constrained to fault localization.

The main fix belongs in [ssh.py](/app/lib/ansible/plugins/connection/ssh.py). `_build_command` reads several settings from PlayContext or core constants instead of `get_option()`; `_ssh_retry` reads the core retry constant; and `_file_transport_command` selects methods from PlayContext and a core constant. The plugin’s option definitions also lack `transfer_method` and `timeout`.

In the same file, `reset()` checks a parsed local `ControlPath` before sending `-O stop`. That check can disagree with the effective SSH arguments. It should check for the persistent connection using the same resolved parameters, skip stop with a debug message when absent, and stop it when present.

The duplicated SSH settings are in [base.yml](/app/lib/ansible/config/base.yml). Before removing them, account for remaining references in [play_context.py](/app/lib/ansible/playbook/play_context.py) and [ssh_functions.py](/app/lib/ansible/utils/ssh_functions.py). Existing [SSH unit tests](/app/test/units/plugins/connection/test_ssh.py) exercise constants based transfer and retry behavior but do not cover reset; no tests were run.

One remaining design detail is how `scp_if_ssh` should act when `transfer_method` has no explicit value. The current code treats it as a fallback, so that behavior needs to be preserved deliberately while moving both settings to plugin resolution.