Fixed contact date parsing so timezone-bearing ISO timestamps retain their written calendar day when serialized to vCard. Added a regression for `2023-12-03T00:30:00+02:00`; the existing text-date import paths use the parser.

`check-types` passed. The shared test suite ran 872 tests in the installed Chromium: 870 passed, including the contact tests. Two unrelated tests failed in the cookie helper and `toBase64`.

**TEST_ENVIRONMENT_PROBLEM:** The configured Playwright Chromium cannot execute because its system loader is missing. I ran the suite with the installed Chromium through a local test override.