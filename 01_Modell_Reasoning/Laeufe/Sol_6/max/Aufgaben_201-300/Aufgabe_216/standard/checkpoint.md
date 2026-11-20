# SSH connection option resolution checkpoint

- Working in `/app` on the SSH connection configuration and persistent reset issue.
- Located the plugin at `lib/ansible/plugins/connection/ssh.py`, core configuration at `lib/ansible/config/base.yml`, and existing unit tests at `test/units/plugins/connection/test_ssh.py`.
- SSH command, transfer, retry, timeout, and reset decisions now read effective plugin options. CLI resolution uses explicit parsed values through the config manager, below variables/keywords and above environment/config.
- Removed SSH-specific definitions from core configuration. Legacy PlayContext and smart transport defaults now resolve the SSH plugin definitions.
- Reset probes the configured connection with `ssh -O check`; it logs and skips `stop` when the probe fails.
- Added regression coverage for config/env/CLI/inventory precedence, transfer fallback, task timeout/retry collisions, and reset commands.
- Verification: 160 relevant unit tests passed with `--forked` to isolate CLI test globals; `ansible-doc -t connection ssh --json` loaded the updated metadata; `git diff --check` passed.
