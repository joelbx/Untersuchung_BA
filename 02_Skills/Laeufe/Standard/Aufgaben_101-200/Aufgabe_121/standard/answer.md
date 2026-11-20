Registered `flipt.is_auth_method(input, "jwt")` for both authorization engines. It accepts the seven supported labels, maps `k8s` and `kubernetes` to the same enum value, returns a boolean for matches, and reports the required errors.

The authz engine tests and `git diff --check` pass.