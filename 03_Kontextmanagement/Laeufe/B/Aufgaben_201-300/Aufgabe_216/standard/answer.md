Resolved the SSH connection issue in `/app`. SSH settings now use the plugin’s option precedence, file transfers use the resolved method, and reset checks the effective socket before sending `stop`. SSH-specific core definitions were removed.

Validation: 23 relevant unit tests passed, and `git diff --check` passed.