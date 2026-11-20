Updated module shebang handling so versioned Python paths, custom paths, interpreter arguments, and non-Python shebangs are preserved. Explicit interpreter task variables still take precedence, and the encoding line is placed immediately after the shebang.

The focused module tests pass: **43 passed**.