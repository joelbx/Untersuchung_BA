Fixed the OIDC login issue. Session domain validation now stores only the hostname and propagates URL parsing errors. OIDC state and token cookies omit the `Domain` attribute for `localhost`, and callback URLs remove one trailing slash from the host before adding the callback path.

Focused tests reproduced the failures before the changes. The full config and OIDC package tests now pass.