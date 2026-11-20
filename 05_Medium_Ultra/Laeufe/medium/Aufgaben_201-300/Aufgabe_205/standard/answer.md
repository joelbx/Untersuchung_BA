Implemented the token lifecycle interface in [src/api/utils.js](/app/src/api/utils.js), including creation and ownership indexes, metadata updates, deletion, and last-seen tracking. Authentication now accepts tokens generated through that interface while continuing to accept existing settings tokens.

Added lifecycle and authentication coverage. ESLint and the focused Mocha run passed: 7 tests.