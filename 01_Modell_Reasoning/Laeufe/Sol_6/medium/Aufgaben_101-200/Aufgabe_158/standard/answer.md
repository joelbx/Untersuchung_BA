Fixed `unarchive` so invalid ZIP timestamps, including `19800000.000000`, fall back to the ZIP epoch instead of raising `ValueError`. Valid timestamps retain daylight saving time handling.

Added a regression test and timestamp boundary tests. All 13 relevant unit tests pass.