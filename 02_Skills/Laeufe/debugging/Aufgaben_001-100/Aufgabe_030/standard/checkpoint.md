# AIX processor facts checkpoint

Task: correct AIX hardware processor fact mappings.

Root cause: `AIXHardware.get_cpu_facts` counted `Available` lines from `lsdev -Cc processor` into `processor_count`, assigned `lsattr ... smt_threads` to `processor_cores`, stored the CPU type as a string, and never computed threads per core or vcpus. With no Available device, its `cpudev` variable could be unset. Linux hardware facts use a processor list and compute vcpus from counts.

Reproduction before fix: `PYTHONPATH=lib:test python -m pytest -q test/units/module_utils/facts/hardware/test_aix_get_cpu_facts.py` exited 1 with 2 failing parameter cases: 12 available devices and SMT output 4 (or absent) yielded incorrect count, cores, processor type, and missing facts.

Fix: count available devices as cores, use constant processor count 1, default threads per core to 1 or read `smt_threads`, calculate vcpus, and wrap CPU type in a list. If no devices are available, return zero cores and vcpus with the default thread count.

Verification: `PYTHONPATH=lib:test python -m pytest -q -o reruns=0 test/units/module_utils/facts/hardware test/units/module_utils/facts/test_facts.py` exited 0: 109 passed, 5 skipped. `git diff --check && python -m compileall -q lib/ansible/module_utils/facts/hardware/aix.py test/units/module_utils/facts/hardware/test_aix_get_cpu_facts.py` exited 0.
