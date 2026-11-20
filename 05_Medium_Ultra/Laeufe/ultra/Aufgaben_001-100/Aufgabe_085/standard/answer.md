Diff reports now mark newly detected CVEs with `+` and resolved CVEs with `-`. `-diff` shows both; `-diff-plus` and `-diff-minus` select either side. Diff entries carry a serialized status, use package data from the corresponding scan, and display their status across report formats. I also added `CveIDDiffFormat` and `CountDiff`.

Three subagents handled the comparison, caller options, and renderers; I integrated their changes. Offline tests passed for `./models ./report ./subcmds ./config`, and `git diff --check` passed.

One limitation remains: if a new and a resolved CVE affect the same package name with different versions, the existing `ScanResult.Packages` map can hold only one version. The current scan version takes precedence.