Fixed the OIDC login flow. Session domains now resolve to a hostname without a scheme or port, both OIDC cookies omit `Domain` for `localhost`, and callback URLs have a single slash after a host with one trailing slash.

Added regression tests. The config and OIDC package tests passed with dependency downloads disabled; `git diff --check` also passed.