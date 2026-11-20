# Checkpoint

Task: reject admin file uploads when the requested destination directory does not exist, using the configured upload path as the base, returning HTTP 500 with `[[error:invalid-path]]` consistently.

Repository: NodeBB. Investigation in progress; next identify upload controller and current tests/error handling, then edit and run focused existing tests.
