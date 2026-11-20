Fault localization complete. Focused existing tests: 113 passed (test_load_book.py and test_utils.py). No project source or tests changed.

Likely faults:
- load_book.py remove_author_honorifics accepts/mutates an author dict rather than taking/returning a name string; exceptions are a dict, exact casefold only; prefix matching has no token boundary and can empty honorific-only names. build_query calls it with the whole author dict.
- find_author stops at the first nonempty name/alternate query before date filtering; an incompatible exact-name result prevents fallback. Surname query compares raw birth/death strings with equality and runs even when complete valid years are absent. Asterisks in input names are passed as wildcard query syntax.
- find_entity filters by birth field presence and author_dates_match, whose missing-date tolerance and string prefix comparison are inconsistent with strict extracted-year matching. Non-person branch bypasses date validation. Comma-name branch computes flipped_name but never puts it in author_flipped_name.
- import_author copies only a whitelist of fields for a new author, conflicting with preservation of all input fields.
- core/helpers.py extract_year already returns the first four-digit run in a string, but is not used by the matching path.

Implementation behavior to cover: case/punctuation-insensitive honorific exceptions, whole-token leading honorific stripping while preserving honorific-only names; staged exact, alternate, then surname searches with birth/death year comparison before advancing; surname fallback only with two valid input years; escaped literal asterisks in input names and wildcard year predicates; new author fields/name preserved. Query escaping needs checking against both real Infobase LIKE conversion and MockSite regex matching.
