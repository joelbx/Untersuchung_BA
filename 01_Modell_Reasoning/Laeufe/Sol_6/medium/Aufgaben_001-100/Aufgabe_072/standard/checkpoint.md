# Checkpoint

Task: implement Punycode URL handling and link handler notification.
Status: source changes complete; URL helper tests and component type check pass. Final lint check in progress.
Changes: URL regex hostname extraction; hostname-only Punycode conversion preserving URL components; link handler uses conversion for external links and notifies on missing or invalid targets.
Constraints: local code and existing tests only; git history and index baseline untouched.
