Task: Support keyword arguments for the Ansible min and max filters through Jinja2 enhanced filters, with Python fallback and clear errors.
Status: Implemented Jinja2 do_min/do_max dispatch with environment context and complete keyword forwarding. Missing enhanced filters use Python built-ins without keywords and raise the requested AnsibleFilterError with keywords.
Verification: 66 filter unit tests passed (test_mathstuff.py and test_core.py); git diff --check passed.
Constraints: Local repository only; preserve git history, index baseline, and harness configuration.
