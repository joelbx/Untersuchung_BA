Updated author matching so exact names, alternate names, and surnames are checked in order using extracted birth and death years. Honorific removal now handles the supported forms and exceptions, asterisks in names no longer act as search wildcards, and new author records retain their input fields.

Relevant tests: **264 passed, 1 expected failure**. Ruff lint and `git diff --check` passed.