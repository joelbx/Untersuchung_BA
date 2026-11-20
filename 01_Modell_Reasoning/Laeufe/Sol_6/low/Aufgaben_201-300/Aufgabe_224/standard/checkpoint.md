Task: Relocate color interpolation helpers to qtutils and update progress indicator call sites.
Status: Implemented in checked-out files. Moved existing interpolation tests to qtutils tests and added checks for None color space percentage validation and output spec.
Verification: 20 interpolation tests pass; combined utils test run reported 304 passed, followed by an X server shutdown error outside pytest.
