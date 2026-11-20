Issue: Support Jinja2 advanced min/max filter arguments in Ansible's mathstuff filters.

Plan: Inspect existing compatibility imports and tests, implement environment-aware dispatch with the required fallback/error behavior, then run relevant existing tests.

Implemented environment-aware min/max dispatch to Jinja2 do_min/do_max, passing through keyword arguments and retaining built-in fallback with the requested legacy error. Added unit coverage for attribute selection. Relevant existing unit file passed: 51 passed using PYTHONPATH=/app/lib (checkout module). A default invocation imported /usr/local Ansible; that run is not representative.
