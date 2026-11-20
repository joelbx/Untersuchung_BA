VERDICT: FIX
Reviewed the applied monitoring patch and production Compose/startup paths. Relevant tests executed: `python -m pytest -q scripts/monitoring/tests/test_utils_py.py scripts/monitoring/tests/test_haproxy_monitor.py scripts/monitoring/tests/test_utils_sh.py` -> 8 passed in 0.13s. `git diff --check` -> passed.
Code defect: the legacy, still-tested `@limit_server` outer decorator order registers a disallowed job before removing it (utils.py:116-118; test_utils_py.py:46-53), contrary to the requirement to skip registration. Make host filtering happen before the scheduler decorator is invoked, and update call sites/tests to use that contract.
Code defect: monitor_haproxy (monitor.py:89-94) is an interval-60s APScheduler job but awaits haproxy_monitor.main(), whose loop never returns (haproxy_monitor.py:97-121). Later firings will hit APScheduler's max_instances limit and be skipped. Run the collector as one explicit background task or make each scheduled invocation bounded.
TEST_ENVIRONMENT_PROBLEM: none.
No project code or tests changed by this review.
