Task: Fix password lookup key=value parameter handling in /app.
Status: Complete. Parameter parsing now uses LookupModule options, preserves inline precedence, and supports string or list chars values.
Verification: Password lookup unit tests passed (32); lookup_password integration playbook passed (31 tasks, 0 failures).
