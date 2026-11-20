Updated the dark mode mapping so Qt 6.4 and later emit `("ForegroundBrightnessThreshold", "100")` for a text threshold of `100`. Earlier Qt versions retain their existing key.

The relevant test suite passed: 42 tests.