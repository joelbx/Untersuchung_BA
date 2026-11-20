Fixed the OIDC login flow. Validation now stores only the hostname in `Session.Domain`; localhost state and token cookies omit the `Domain` attribute; and callback URLs have one slash between the host and callback path. The state cookie remains scoped to the provider’s callback path.

Added focused tests. Both relevant Go packages pass with downloads disabled, and `git diff --check` passes.