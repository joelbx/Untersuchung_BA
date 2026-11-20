The patch now makes `oval.major("")` return `""` and adds the three required public functions in [report/report.go](/app/report/report.go).

All three reviewer test targets pass with offline dependencies and `GOFLAGS=-p=1`; `git diff --check` passes. The first parallel test run hit the container’s process limit, but the sequential rerun passed. No failures remain.