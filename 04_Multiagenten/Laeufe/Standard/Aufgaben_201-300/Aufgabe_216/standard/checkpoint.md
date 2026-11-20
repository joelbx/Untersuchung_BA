Task: Resolve SSH connection option precedence and persistent reset detection.
Status: Implemented plugin-based option resolution, removed duplicate core SSH settings, updated transport selection and persistent reset probe. SSH and PlayContext tests pass (24 tests).
Validation: PYTHONPATH=lib:test python -m pytest -q test/units/plugins/connection/test_ssh.py test/units/playbook/test_play_context.py
Additional config manager suite has pre-existing Python 3.9 fixture errors assigning None to os.environ[ANSIBLE_CONFIG].
