Task: Correct QtColor HSV/HSVA percentage parsing and function validation.
Status: Implementation and regression tests complete.
Changes: Hue percentages scale by 359/100; other percentage components scale by 255/100 with exact 100% endpoints. Color function name and arity are validated before parsing. RGB/RGBA and nonpercentage conversion behavior remains intact.
Verification: 54 focused QtColor/QssColor tests passed. git diff --check passed. Broader test_configtypes.py run excluding Hypothesis: 976 passed, 20 xfailed, 4 unrelated failures (Qt warnings for Proxy, QtFont float weight, TimestampTemplate validation). Full run also encounters pre-existing Hypothesis function-scoped fixture health check.
