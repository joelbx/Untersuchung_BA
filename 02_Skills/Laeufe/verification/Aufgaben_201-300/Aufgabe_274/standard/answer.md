Updated `qt.workarounds.disable_accelerated_2d_canvas` to accept `always`, `auto`, and `never`, with `auto` as the default. In `auto`, the flag is added only on Qt 6 with a known Chromium major version below 111.

Verification: 573 relevant tests passed, 1 was expected to fail, and Python compilation and `git diff --check` passed. Lint remains unverified because `flake8` is not installed.