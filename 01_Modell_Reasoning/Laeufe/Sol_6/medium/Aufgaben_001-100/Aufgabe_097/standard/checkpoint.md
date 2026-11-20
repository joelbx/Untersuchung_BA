# Checkpoint

Task: Raise the controller Python minimum and update collection extraction behavior.
Status: Implemented Python 3.12 controller minimum, removed collection tar member cache and other controller compatibility branches, and updated metadata and changelog. Python 3.10 and 3.11 remain supported on targets.
Verification: 159 unit tests passed, 1 skipped across collection extraction/install, collection loader, role install, and CLI. Both controller entry points reject Python 3.11 with identical messages. Tests ran with the import gate bypassed in memory because this environment only has Python 3.11.
