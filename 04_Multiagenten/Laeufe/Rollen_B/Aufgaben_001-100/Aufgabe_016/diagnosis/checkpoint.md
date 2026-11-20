Fault-localization progress (complete):
- scripts/monitoring/utils.py defines OlBlockingScheduler, not required OlAsyncIOScheduler; add_job already defaults the id to func.__name__, and listener events are present.
- limit_server reads HOSTNAME via os.environ.get, supports exact/wildcard/FQDN-short matching, but executes after the inner scheduled_job decorator has registered the job and removes it on disallowed hosts. To truly skip registration, decorator composition or registration API must change. Its assert on missing HOSTNAME is another edge case.
- scripts/monitoring/monitor.py uses synchronous jobs and starts BlockingScheduler at module import; an async main and HAProxy job require restructuring.
- scripts/monitoring/haproxy_monitor.py and get_service_ip are absent. Existing test_utils_py.py tests four host-match cases with OlBlockingScheduler but not the new async interfaces or registration timing. Targeted existing test run: 2 passed.
- No project source or tests edited.
