Updated [play.py](/app/lib/ansible/playbook/play.py) so `Play.load` leaves the input unchanged, `get_name` derives a name from hosts when needed, and host validation raises the requested parser errors.

Added focused coverage in [test_play.py](/app/test/units/playbook/test_play.py). The relevant unit tests pass: **13 passed**. `git diff --check` also passes.