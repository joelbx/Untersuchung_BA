VERDICT: FIX

Code defect: `lib/ansible/plugins/shell/powershell.py:122-138` groups adjacent `<Objs>` elements and parses them as one block. If a valid element is immediately followed by a malformed closed element, `_parse_clixml` raises on the latter and the helper leaves both unchanged. Reproduced with `#< CLIXML\r\n<Objs Version="1"><S S="Error">good</S></Objs><Objs Version="1"><S S="Error">bad</Objs>`: actual is the full raw input; expected is `good` followed by the malformed element unchanged. Parse elements separately, preserving the failing element and continuing after it.

Relevant existing tests: `PYTHONPATH=lib python -m pytest -q test/units/plugins/shell/test_powershell.py test/units/plugins/connection/test_ssh.py` -> 46 passed in 0.44s. The uncovered mixed valid/invalid adjacent case above fails manual reproduction. No TEST_ENVIRONMENT_PROBLEM.
