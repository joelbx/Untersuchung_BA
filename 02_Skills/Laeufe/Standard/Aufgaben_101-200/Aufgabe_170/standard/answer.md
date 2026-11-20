Updated edition matching so `editions_match` and the new `threshold_match` expand raw records before scoring. The shared expansion now builds title variants, combines ISBN fields, enriches author and contributor names, and filters invalid publish countries.

The targeted tests passed: **67 passed, 2 existing expected failures**. `git diff --check` also passed.