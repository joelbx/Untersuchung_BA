Updated the Qt 6.4 dark mode mapping so a text threshold of `100` emits `("ForegroundBrightnessThreshold", "100")`. Earlier Qt versions retain their existing key.

Added regression coverage and verified the focused test suite: **41 passed**.