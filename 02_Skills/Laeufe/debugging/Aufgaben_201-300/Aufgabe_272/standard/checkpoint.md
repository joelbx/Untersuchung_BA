# Checkpoint

Issue: custom TLS cipher suites across URL helpers, get_url, uri, and url lookup.
Status: investigating root cause before changes.
Environment: `rg` unavailable (`/bin/bash: rg: command not found`); using grep/find.

Root cause: validated HTTPS builds a context through SSLValidationHandler.make_context, while validate_certs=False builds a separate SSLContext in Request.open. No cipher input exists at either path or the public wrappers. HTTP-to-HTTPS redirect uses the opener's CustomHTTPSHandler context, so a cipher context must be installed even for an initial HTTP URL.
Pattern: url_argument_spec supplies both get_url and uri; fetch_url reads module params; lookup forwards options to open_url; Request.open owns handlers.
Hypothesis: a shared make_context plus explicit ciphers propagation will apply one context to direct, proxy, Unix socket, and redirect HTTPS paths. Existing test reproduction fails with missing make_context (command: PYTHONPATH=lib python -m pytest -q test/units/module_utils/urls/test_urls.py -k 'test_make_context_ciphers or test_make_context_invalid_ciphers').

Verification note: PyOpenSSL adapter source could not be inspected in this environment. Command: `python - <<'PY'\nfrom urllib3.contrib.pyopenssl import PyOpenSSLContext\nimport inspect\nprint(inspect.getsource(PyOpenSSLContext.set_ciphers))\nPY`; error: `ModuleNotFoundError: No module named 'OpenSSL'`. The PyOpenSSL-specific branch remains unverified locally; native SSLContext tests cover the target Python 3.10/OpenSSL path.

Implementation: public get_ca_certs and make_context; ciphers validated and applied through Request, open_url, fetch_url, module argument spec, get_url, uri, and lookup url. HTTPS handlers share the context, including initial HTTP URLs that can redirect to HTTPS and Unix socket handling. Unsupported values raise sanitized ValueError; disabled validation retains SSLv2/SSLv3 exclusion.
Final checks: `PYTHONPATH=lib python -m pytest -q --override-ini='reruns=0' test/units/module_utils/urls test/units/plugins/lookup/test_url.py` passed (129 tests before final explicit module call-site change). `python -m py_compile lib/ansible/module_utils/urls.py lib/ansible/modules/get_url.py lib/ansible/modules/uri.py lib/ansible/plugins/lookup/url.py` passed. `git diff --check` passed. Rechecking after final module call-site change.
Final recheck after all edits: `PYTHONPATH=lib python -m pytest -q --override-ini='reruns=0' test/units/module_utils/urls test/units/plugins/lookup/test_url.py` passed, 129 tests; `python -m py_compile lib/ansible/module_utils/urls.py lib/ansible/modules/get_url.py lib/ansible/modules/uri.py lib/ansible/plugins/lookup/url.py` passed; `git diff --check` passed. Three existing deprecation warnings appeared.
