Fixed YAML dumping of `AnsibleUndefined`: it now raises the missing-variable error instead of a PyYAML representation error. Both YAML filters report which filter failed and preserve the original exception for inspection.

Added dumper, filter, and template regression tests. **Verification:** 64 relevant tests passed; `git diff --check` passed.