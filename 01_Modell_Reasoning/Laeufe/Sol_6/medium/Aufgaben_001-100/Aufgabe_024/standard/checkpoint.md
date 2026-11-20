Task: Fix catalog author matching across date formats, honorifics, and literal asterisks.
Status: Complete. Updated staged author lookup to compare extracted birth/death years, escape name asterisks, and use surname/year wildcard queries only with two valid years. Honorific helper now takes and returns a string; new author candidates retain input fields. Mock search honors escaped asterisks.
Verification: 142 relevant pytest cases passed; ruff check passed; git diff --check passed.
Constraints observed: Local code/tests only; no git history, index, or harness configuration changes.
