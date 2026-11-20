Task: Fix unarchive ZIP timestamp parsing for invalid and out-of-range dates.
Plan: inspect current ZIP handling and tests, add timestamp sanitizer, run relevant existing tests.
Status: sanitizer and regression cases implemented; unarchive unit suite passed (14 tests). No delegation used.
