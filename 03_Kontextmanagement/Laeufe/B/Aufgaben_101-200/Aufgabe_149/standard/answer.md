Updated [qtargs.py](/app/qutebrowser/config/qtargs.py) to recognize both feature prefixes. Enabled features are merged into one `--enable-features=` argument; each `--disable-features=` argument is passed through unchanged. Added coverage for command line, configuration, and disable-only cases.

Validation: **87 Qt argument tests passed**; `git diff --check` passed.