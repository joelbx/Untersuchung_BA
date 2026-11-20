Correction round: inspected current patch. Reviewer reports crypt-backed bcrypt ident=2 fails on host; existing test mocks crypt and misses it. Next: inspect backend capabilities and add real fallback plus unmocked regression, then rerun flagged tests.
Confirmed host crypt returns '*0' for $2$, while installed passlib generates valid $2$ hash. Added fallback on crypt rejection and unmocked regression exercising crypt-selected path.
Final: both reviewer test commands rerun after fix; 50 passed and 7 passed. No remaining test failures or prepared dependency issues.
