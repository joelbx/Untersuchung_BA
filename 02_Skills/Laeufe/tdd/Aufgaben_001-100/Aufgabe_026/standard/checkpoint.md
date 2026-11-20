Task: fix multi-source CVE handling for OS families.
Status: implemented and verified.
Red checks: new mapping was undefined; Ubuntu API change detector test failed; Oracle/Fedora/Microsoft CVSS tests returned no scores.
Green checks: GOPROXY=off GOSUMDB=off go test ./models ./reporter ./detector -run targeted tests -count=1; GOPROXY=off GOSUMDB=off go test ./... passed.
Offline tooling: no check blocked.
