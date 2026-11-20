Task: Make absent collection manifest distinct from explicit empty/null manifest configuration.
Completed: Metadata uses Sentinel for an absent manifest; builder uses the walk for Sentinel and directive handling for explicit empty/null values. The walk applies ignore patterns and excludes external file and directory symlinks while retaining internal links.
Validation: PYTHONPATH=lib python -m pytest -q test/units/galaxy (213 passed). git diff --check passed.
