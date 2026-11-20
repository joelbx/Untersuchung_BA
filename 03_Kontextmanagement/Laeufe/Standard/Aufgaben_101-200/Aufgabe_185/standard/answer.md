Updated the expiry utility to use the current subscription term during cancellation or when renewal is disabled. Cancellation screens now display that active term’s end date, while scheduled plan behavior remains available when renewal is enabled. Free plan output is unchanged.

All 44 relevant tests passed across four suites, and `git diff --check` found no issues.