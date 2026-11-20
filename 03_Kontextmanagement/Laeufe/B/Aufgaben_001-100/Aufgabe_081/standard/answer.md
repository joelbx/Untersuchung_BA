Resolved the OIDC login issue in the checked-out files. Session domains now normalize to hostnames, localhost cookies omit the `Domain` attribute, and callback URLs remove one trailing slash from the host.

The existing config and OIDC package tests passed with network module lookup disabled.