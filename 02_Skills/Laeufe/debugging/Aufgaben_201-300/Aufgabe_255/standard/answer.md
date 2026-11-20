Updated the password lookup to parse inline key=value parameters through the lookup instance, with term values taking precedence over plugin options. `chars` now accepts either a list or a comma-separated string, including `,,` for a literal comma.

Verification passed: 34 password unit tests and the local lookup-password playbook, including its repeated-seed checks.