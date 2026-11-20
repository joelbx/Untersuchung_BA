Added `/proc/sysinfo` parsing for IBM Z hardware facts and included its values in `setup` results after DMI collection. The method returns `{}` when the file is absent and keeps undiscovered fields as `NA`.

All 18 relevant unit tests pass, including the new parsing and collection tests. `git diff --check` passes.