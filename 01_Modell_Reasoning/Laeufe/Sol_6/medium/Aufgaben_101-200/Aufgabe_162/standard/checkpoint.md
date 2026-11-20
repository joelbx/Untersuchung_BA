Task: Add optional encoding validation to FormatString during to_py conversion.
Status: Implemented optional encoding validation in FormatString, configured ASCII for content.headers.user_agent, and added type/configuration tests. Verification: configtypes.py and configdata.py suites passed (1139 passed, 10 xfailed); focused follow-up passed (15 passed); git diff --check passed.
