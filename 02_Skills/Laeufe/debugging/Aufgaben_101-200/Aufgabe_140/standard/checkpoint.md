# Checkpoint

Task: fix hosts blocking of parent domains for subdomain requests.

Root cause: HostBlocker._is_blocked compared only the exact QUrl host with the runtime and config blocked sets. It did not check parent domains. A private hostname-widening helper already existed in configutils; the requested public interface was absent from urlutils. The old per-URL test used a relative QUrl with an empty host, so its positive assertion relied on inserting an empty string into the block set.

Regression evidence: New parent-domain tests failed for runtime and config sets at sub.example.com. The new urlutils interface tests failed because widened_hostnames was absent. A trailing-dot blocked entry also failed to match a non-trailing request before the final lookup adjustment.

Patch: Add urlutils.widened_hostnames, share it with configutils, check the blocking toggle and whitelist before iterating widened request hosts, and match trailing-dot variants in either blocked set. Correct the per-URL test to use a full request URL.

Verification: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/components/test_hostblock.py tests/unit/utils/test_urlutils.py tests/unit/config/test_configutils.py -o reruns=0 --disable-warnings` passed: 426 passed, 1 skipped. `git diff --check` passed.
