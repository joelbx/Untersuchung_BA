# Checkpoint

Task: Replace BlocklistDownloads callback completion API with Qt signals, update consumers/tests, and run existing relevant tests.

Initial inspection: implementation is in qutebrowser/components/utils/blockutils.py; consumers are in components/adblock.py and components/braveadblock.py; tests are in tests/unit/components/test_blockutils.py.
