VERDICT: FIX
Code defect: detector/detector.go:335 unconditionally calls detectPkgsCvesWithGost after OVAL for Red Hat families. gost/gost.go:63-67 opens the configured Gost DB before selecting Pseudo, so a missing or broken Gost DB still aborts Red Hat package CVE detection. Correction: skip Gost package detection for Red Hat, CentOS, Alma and Rocky (or bypass Gost DB initialization for these families).
Tests: GOPROXY=off GOSUMDB=off go test ./oval ./gost -> PASS; GOPROXY=off GOSUMDB=off go test ./detector -> PASS. No TEST_ENVIRONMENT_PROBLEM.
