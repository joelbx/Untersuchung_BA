The role patch already handles validation and equality as requested. I fixed the remaining test failure by having the self-signed certificate test generate a current certificate instead of reading the fixture that expired in 2021.

All three reviewer-flagged test commands now pass, including the full `./lib/utils` suite. `git diff --check` also passes.