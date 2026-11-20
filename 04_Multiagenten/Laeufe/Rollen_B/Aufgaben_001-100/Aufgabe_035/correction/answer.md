Fixed the reviewer’s defect: numeric and boolean comparisons now return parse errors for empty or whitespace-only context values. I updated the affected tests, including the evaluation case with a missing boolean value.

`GOPROXY=off GOSUMDB=off go test ./server ./storage` and `git diff --check` pass. No remaining failures.