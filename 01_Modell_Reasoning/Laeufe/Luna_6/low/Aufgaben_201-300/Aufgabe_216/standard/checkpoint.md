Task: fix SSH connection option sourcing and persistent socket reset parameter consistency.

Plan: inspect plugin options and core config definitions; identify existing unit tests; move/configure supported settings through SSH plugin get_option() and use effective values in command, transfer, retries, reset; update focused tests only as needed; run relevant existing tests.
