# Checkpoint

Task: ensure oval.major("") returns "" while preserving non-empty behavior.
Change: added an exact-empty guard in oval/util.go and a regression case in oval/util_test.go.
Verification: git diff --check, focused Test_major, and full ./oval tests passed (GOPROXY=off).
