Fixed the OIDC login flow. Authentication validation now stores only the hostname in `Session.Domain`; OIDC state and token cookies omit the `Domain` attribute for localhost; and callback URLs remove one trailing host slash before adding the callback path. Added regression tests for these cases.

The config and OIDC package tests pass, and `git diff --check` is clean.