The checked-out patch resolves the issue: `interpolate_color` and its helper are in `qtutils`, and the download and tab progress call sites use it. I found no further code defect, so I made no project code changes in this correction round.

I reran all three reviewer test commands successfully: 20, 28, and 307 passed. `git diff --check` also passed.