Implemented the Windows SSH stderr fix. Valid CLIXML blocks are decoded in place, with UTF-8 and cp437 support; surrounding bytes and invalid or incomplete blocks are preserved. The UTF-16-BE escape matcher is also corrected.

Validation: **48 relevant tests passed**, and `git diff --check` passed.