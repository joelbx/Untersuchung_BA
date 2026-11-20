# Checkpoint

Task: Resolve the ansible-core compatibility and behavior issues described in the repository request.

Constraints: Use local repository code and existing tests only; do not fetch or delegate; do not read credentials, private process files, benchmark solutions, or evaluator artifacts; do not change git history, index baseline, or harness configuration.

Completed changes: Added a shared `_UNSET` sentinel and migrated internal missing-value defaults/checks; clarified missing module args; updated `fail_json`; made legacy YAML constructors match native zero-argument, mapping, string/bytes, and iterable construction; ignored `None` templating overrides; corrected lookup warning/log-only messages; gated module-returned deprecations by global config and ensured the disable note appears; made `timedout` return a Boolean; included AnsibleError help text and its exit code for early CLI failures.

Verification: `git diff --check` passed. Focused existing suites passed: 463 passed, 1 skipped. The deprecation utility suite's `test_dedupe_with_traceback` was deselected after it failed in the repository's controller-mode test setup (the test expects target-side accumulation); the other tests in that file passed.
