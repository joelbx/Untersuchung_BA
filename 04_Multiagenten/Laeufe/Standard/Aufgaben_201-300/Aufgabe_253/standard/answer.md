Updated `GUIProcess` to show stdout and stderr while the process runs, with stderr shown at error severity. On completion, it summarizes each nonempty stream, always placing stdout before stderr. Empty streams produce no messages.

The relevant tests pass: **41 passed**.