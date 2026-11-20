# Checkpoint

Issue: Add an application feature flag for QR sign-in, default disabled, and gate QR sign-in entry points on the setting plus MSC3882/MSC3886 support.

Plan:
1. Inspect settings definitions, QR components, and existing focused tests.
2. Add the experimental setting and gate component rendering/action on it.
3. Update/add focused tests and run the repository's existing relevant test commands.

Constraints: preserve existing user changes, do not modify git history, index baseline, or harness configuration.
