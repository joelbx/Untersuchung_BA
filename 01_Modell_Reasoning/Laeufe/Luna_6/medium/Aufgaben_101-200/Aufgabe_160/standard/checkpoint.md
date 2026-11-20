# Checkpoint

Task: Fix Direct Dial node wildcard address reporting by carrying the stream peer address into SSH heartbeat handling.

Plan:
1. Locate repository guidance, inventory stream interfaces/pipe, and SSH heartbeat controller.
2. Implement peer address option and rewrite wildcard heartbeat host while preserving its port.
3. Run relevant existing tests and record results.
