Fixed `ansible-doc` wrapping so `HORIZONTALLINE` stays on its own 13-dash line in CLI output, including option descriptions, the main description, and notes. Added a regression test for the option description.

The reviewer’s exact test command passed: **32 passed**. `git diff --check` also passed.