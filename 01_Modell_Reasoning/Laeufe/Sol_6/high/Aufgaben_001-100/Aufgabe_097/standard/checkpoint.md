# Controller Python minimum update

Working in `/app`. Initial repository status was clean.

Implemented the Python 3.12 controller minimum in CLI entry points, package metadata, and ansible-test's controller matrix. Python 3.10 and 3.11 remain in the remote-only matrix. Removed the collection TarFile private cache and changed directory extraction to direct `getmember(dirname)` lookup with the required error. Simplified obsolete controller compatibility branches and collection-loader Python 2 fallbacks. Added a breaking-change fragment.

Verification on available Python 3.11: collection extraction and loader tests 73 passed, 1 skipped; ansible-test unit tests 10 passed; role requirements tests 11 passed. Both `ansible` and `ansible-test` print the same 3.12 minimum error. `py_compile` and `git diff --check` passed. Python 3.12 is unavailable locally, so full controller runtime tests cannot run here.
