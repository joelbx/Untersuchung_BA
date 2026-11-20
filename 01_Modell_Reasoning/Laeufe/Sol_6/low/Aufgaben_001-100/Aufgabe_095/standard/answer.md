Added the importable `make_date_string` function with zero-padded month and day formatting, and added `patron_check_ins.is_valid` to require an `id` plus either `year` or `data`. Existing instance calls to the formatter still work.

The check-ins test file passes: **7 tests passed**.