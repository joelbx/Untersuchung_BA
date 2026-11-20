Task: Add filesystem path completion for :open.

Implemented `FilePathCategory`, wired it into the configured open category order, and added `completion.favorite_paths` plus filesystem valid/default documentation.

Verification: `py_compile` and `git diff --check` pass. The focused existing completion tests mostly pass, but `test_url_completion_no_quickmarks` fails because its fixture's open categories use production defaults and it asserts there are only two categories; the new required filesystem category makes three. The relevant explicit category tests pass. Existing tests were not edited.
