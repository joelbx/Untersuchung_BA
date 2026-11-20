The failure spans three paths:

- [config/os.go](/app/config/os.go:330) maps every single-token release, including `2023`, to Amazon Linux 1. Its `GetEOL` table has no entries after 2022. The fix should recognize `1`, `2`, `2022`, `2023`, `2025`, `2027`, and `2029`; map `YYYY.MM` to `1`; and leave other releases unknown.
- [scanner/redhatbase.go](/app/scanner/redhatbase.go:266) has 2022-specific parsing. A bare `Amazon Linux release 2023` can enter the broad release-2 branch and panic when it reads a missing field.
- [oval/util.go](/app/oval/util.go:114) selects Amazon OVAL release `1` for anything other than `2` or `2022`, which can send AL2023 vulnerability lookups to AL1. [oval/redhat.go](/app/oval/redhat.go:71) also lacks ALAS2023 advisory link handling.

The EOL comparison methods already handle standard and extended dates separately, but tests need boundary cases for both. **Uncertainty:** the repository does not establish the correct vendor EOL dates for 2023, 2025, 2027, or 2029.

I recorded the findings in [checkpoint.md](/app/.codex-role-output/checkpoint.md). Source and tests were left unchanged under this run’s diagnosis-only scope.