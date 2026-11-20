Fixed both review findings: author matching now compares date years when both records provide them, and a match for the supplied name takes priority over a flipped-name match. Added regression tests for both cases.

The reviewer’s test commands pass: 56 tests in the load-book and helper suites, and 85 in the catalog utils suite. `git diff --check` also passes.