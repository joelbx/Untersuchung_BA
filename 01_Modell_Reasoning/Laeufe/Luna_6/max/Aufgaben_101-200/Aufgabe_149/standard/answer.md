Implemented feature flag handling in [qtargs.py](/app/qutebrowser/config/qtargs.py). Enabled features are combined into one flag; disable flags are forwarded unchanged. The module now exposes both prefix constants.

Verification: focused tests passed (82), and a smoke check confirmed command-line and configuration inputs behave equivalently. `git diff --check` passed.

Checkpoint: [checkpoint.md](/app/.codex-role-output/checkpoint.md)