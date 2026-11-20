The issue is localized to two functions. [CveContent](/app/models/cvecontents.go:272) already has the three requested CVSS v4 fields, so the model needs no extension.

- [ConvertNvdToModel](/app/models/utils.go:102) groups metrics by `Source`, but processes only v2 and v3 and copies only those fields into the resulting records. It should also process `nvd.Cvss40` and copy its score, vector, and severity, including when v4 is the only metric for a source.
- [Cvss40Scores](/app/models/vulninfos.go:612) visits only MITRE. Its source order should be `[Mitre, Nvd]`, retaining its existing rule for skipping empty metrics.

The [existing v4 test](/app/models/vulninfos_test.go:1907) covers MITRE alone; I found no NVD conversion test. I did not verify the dependency’s `Cvss40` field shape, so that remains uncertain. No project source or tests were changed: the workspace instructions restricted this pass to fault localization.