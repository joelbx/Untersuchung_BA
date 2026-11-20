Resolved the repository issue: unset handling now uses `_UNSET`; YAML legacy constructors accept base type construction patterns; templar ignores `None` overrides; lookup and early CLI errors include clearer details; module deprecations respect configuration; and `timedout` returns a Boolean.

Added regression tests. **353 affected unit tests passed**, and `git diff --check` passed.