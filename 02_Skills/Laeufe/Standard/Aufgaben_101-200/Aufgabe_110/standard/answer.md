Added the Drive download mechanism metric and registered it with the existing metrics infrastructure. Terminal download outcomes now include status, retry, and the selected mechanism; preview reports pass file size so the mechanism can be selected consistently.

Verification passed: 20 focused tests, the Drive TypeScript check, Prettier, and `git diff --check`.