Fixed host validation in [Play](/app/lib/ansible/playbook/play.py). `Play.load` no longer changes the play name; `get_name` derives it dynamically, and malformed `hosts` values now produce `AnsibleParserError` messages instead of the reported exception.

Verification: all 247 playbook unit tests passed. A CLI syntax check of the existing empty-hosts fixture returned the expected parser error.