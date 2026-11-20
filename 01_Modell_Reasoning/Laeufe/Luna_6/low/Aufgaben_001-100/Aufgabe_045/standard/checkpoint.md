# Checkpoint

Task: Fix ansible-galaxy collection FQCN validation so Python keywords are rejected, and remove the legacy Python 2/3 identifier helpers in `dataclasses.py`.

Plan:
1. Inspect the validation implementation and focused unit tests.
2. Replace compatibility helpers with `is_python_identifier` and boolean validation that excludes keywords.
3. Run the existing relevant unit tests.
