Fixed the OIDC login flow. Validation now reduces the session domain to a hostname, localhost cookies omit the `Domain` attribute, and callback URLs remove one trailing slash from the configured host before adding the path.

The existing config and OIDC package tests pass.