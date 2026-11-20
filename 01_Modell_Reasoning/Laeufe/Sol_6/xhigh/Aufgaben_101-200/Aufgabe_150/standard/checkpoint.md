Task: accept minimal collection manifest configuration and preserve default file manifest behavior.
Status: implemented and verified. Missing manifest metadata uses Sentinel; explicit empty or null manifest selects default directives. The Sentinel walk applies build_ignore and excludes external file and directory symlinks while retaining internal links.
Verification: PYTHONPATH=lib python -m pytest -q test/units/galaxy test/units/cli/galaxy (237 passed). The local environment lacks distlib, so directive selection was unit tested with a mock.
