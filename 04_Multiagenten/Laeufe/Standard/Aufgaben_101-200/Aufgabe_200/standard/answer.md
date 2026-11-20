Added unit support to `:later`. It now accepts durations such as `5s`, `2m30s`, and `1.5h`; bare integers still mean milliseconds. The new [parse_duration function](/app/qutebrowser/utils/utils.py) validates input and returns milliseconds, and the [command help](/app/doc/help/commands.asciidoc) reflects the new syntax.

Verification: 255 relevant unit tests passed, and `git diff --check` passed.