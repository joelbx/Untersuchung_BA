# Checkpoint

## Objective
Resolve the CLIXML output decoding issue in `/app`.

## Completed
- `_parse_clixml` now has the requested `bytes` / `str` annotations and bytes return type.
- Parses every `<Objs>` block in input order and filters `<S>` elements by the requested stream.
- Concatenates selected stream text within each block, then inserts CRLF only between nonempty block results.
- Decodes four-digit hexadecimal escape tokens, combines valid surrogate pairs, preserves unpaired surrogates using `surrogatepass`, supports lowercase digits, leaves malformed tokens unchanged, and implements `_x005F_` handling.
- Preserves decoded control characters without trimming.
- Updated the existing single-stream expected output for its preserved trailing CRLF.

## Verification
- `python -m pytest -q test/units/plugins/shell/test_powershell.py`: 6 passed.
- `git diff --check`: passed.
