VERDICT: FIX

**Code defect:** [detector.go](/app/detector/detector.go:335) still calls Gost for Red Hat package scans. [gost.go](/app/gost/gost.go:63) opens the Gost database before returning its no-op client, so an unavailable Gost database can abort an otherwise valid OVAL scan. Skip Gost package detection for Red Hat, CentOS, Alma, and Rocky.

**Tests passed:**

- `GOPROXY=off GOSUMDB=off go test ./oval ./gost`
- `GOPROXY=off GOSUMDB=off go test ./detector`

No test environment problem.