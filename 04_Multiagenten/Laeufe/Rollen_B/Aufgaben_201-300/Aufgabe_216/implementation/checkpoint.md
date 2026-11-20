Started implementation. Checking SSH option definitions, runtime reads, and config references before edits.
Verified bypasses in SSH command, transfer, retry, and reset paths. Core timeout is also injected into plugin task keys; handling precedence during plugin option setup.
Implemented plugin option resolution and active-socket reset check; moved core SSH settings into plugin metadata. Repository tests pass with PYTHONPATH=lib (21 SSH tests). Final reference/diff review in progress.
Final verification: PYTHONPATH=lib pytest -q test/units/plugins/connection/test_ssh.py: 22 passed. git diff --check clean; no source references to removed core SSH constants remain.
