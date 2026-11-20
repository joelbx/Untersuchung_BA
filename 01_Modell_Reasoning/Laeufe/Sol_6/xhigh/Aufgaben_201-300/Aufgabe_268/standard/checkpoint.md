Task: Resolve process startup error messages in qutebrowser/misc/guiprocess.py.
Status: Complete. Updated normal and detached start errors to include the process name, command, error type, and detail, with a POSIX executable hint for missing or inaccessible commands.
Verification: 34 guiprocess unit tests pass; git diff --check passes. The targeted spawn end-to-end scenario could not start because QtWebKit is unavailable in the local environment.
