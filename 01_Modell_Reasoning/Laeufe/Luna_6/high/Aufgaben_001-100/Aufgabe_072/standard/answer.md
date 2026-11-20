Implemented Punycode URL handling. External links are converted before hostname checks and confirmation handling; the conversion preserves the URL components and removes trailing slashes from the pathname. The handler also shows an error notification when it can’t extract a URL.

Added helper tests. The focused Jest suite passed: **14 tests**. Prettier and `git diff --check` passed.