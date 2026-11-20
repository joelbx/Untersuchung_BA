Implemented the OS EOL lookup and per-target scan warnings, including the required messages, date boundaries, and summary order. OS family identifiers now sit with the EOL mapping, and major-version parsing is shared across components.

Added focused tests. The full repository test suite and the affected-package tests passed; `git diff --check` passed.