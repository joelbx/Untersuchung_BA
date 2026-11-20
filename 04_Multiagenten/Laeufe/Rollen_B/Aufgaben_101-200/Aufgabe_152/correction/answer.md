Fixed `icx_logging` so host names are stripped before required-field validation. Whitespace-only names now fail validation for both direct and aggregate input. Added a regression test.

The reviewer’s exact test commands pass: 11 logging tests and 103 ICX tests. No remaining failures or TEST_ENVIRONMENT_PROBLEM.