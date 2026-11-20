Progress: inspected the existing drive firmware module and seven tests. Independent review found upgrade_list() considers status but misses offline=True and available=False. Next: add those accessibility checks, cover both fail and skip paths, then rerun the two reviewer test commands.
Implemented accessibility check for offline=True and available=False, plus regression tests for default failure and ignore behavior. Running reviewer tests next.
Reviewer tests rerun: drive firmware 9 passed; E-Series facts 3 passed with 2 pre-existing deprecation warnings. No test environment problem.
