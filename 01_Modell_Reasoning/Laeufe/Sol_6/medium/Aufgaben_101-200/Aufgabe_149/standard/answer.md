Updated the QtWebEngine argument builder to merge all enabled features into one `--enable-features=` flag and pass each `--disable-features=` flag through unchanged. Both command-line and configuration flags are covered, including comma-separated lists.

The focused test suite passed: 90 tests. `git diff --check` passed. Flake8 was unavailable in the environment.