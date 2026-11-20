Task: implement transparent gzip response handling across URL utilities, uri, and get_url.
Status: complete. Added GzipDecodedReader, decompression request options and propagation, missing-gzip fallback, and module documentation/options. Updated URL utility tests for decoding, opt-out, headers, and missing-gzip behavior.
Verification: PYTHONPATH=lib:test pytest -q --reruns 0 test/units/module_utils/urls (85 passed); py_compile for modified library/modules; git diff --check.
Constraints honored: local code/tests only; git history, index baseline, and harness configuration untouched.
