Updated the Windows SSH stderr path to replace embedded CLIXML with readable UTF-8 bytes, using cp437 when UTF-8 decoding fails. Surrounding output and incomplete or malformed blocks are preserved. I also corrected the UTF-16-BE escape regex and added regression tests.

The relevant existing test suites pass: **38 tests**.