Resolved the SSH connection issue. Runtime command, transfer, retry, and reset decisions now use effective plugin options from `get_option()`. Reset checks for an active control socket with those same settings before sending stop. SSH-specific settings were removed from core configuration, and explicit CLI values retain precedence even when they match parser defaults.

**Verification:** 120 relevant tests passed; `git diff --check` passed. A broader config run had eight existing fixture setup errors, while the focused config tests passed.

I delegated the plugin, test, and supporting reference changes to subagents, then reviewed and verified the combined patch.