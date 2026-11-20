Updated `ListRecord.from_input()` to parse URL encoded POST bodies separately from query parameters, apply defaults only where appropriate, and safely normalize nested `seeds` entries. Updated `unflatten()` so later assignments to the same simple key take precedence.

Relevant existing tests passed: 14 tests across the list and upstream utils test modules.