Added `parse_duration` for hour, minute, and second expressions, including decimal values and whitespace between units. Bare integers still mean milliseconds. The `:later` command now uses it, and the command help reflects the new syntax.

The relevant unit test files passed: **191 tests**. No delegation was used.