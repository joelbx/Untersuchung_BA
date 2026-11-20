Fixed the new ESLint formatting error in the enabled chat edit route. The full messaging suite passes (77 tests), and `git diff --check` passes.

The focused `edit/delete` run still fails because it skips the room setup it needs. Changed-file ESLint reports 14 pre-existing errors, with no new route error.

The issue description appears mismatched with this patch: no tracked `DirectedGraph` or `LinkProvider` code exists in the repository.