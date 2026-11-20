# Checkpoint

Task: Fix AIX processor facts so count is constant 1, cores are counted from device-list output, threads per core default to 1 or use the reported value, vCPUs are cores multiplied by threads per core, and processor is a one-item list containing the CPU type.

Constraints: Work only from local repository code and existing tests; do not change git history, index baseline, or harness configuration.

Findings: `AIXHardware.get_cpu_facts()` treated available processor device count as `processor_count`, assigned `smt_threads` to `processor_cores`, and returned the type as a scalar. No dedicated AIX hardware unit test exists.

Change: Updated `get_cpu_facts()` to count available processor devices as cores, return constant processor count 1, parse CPU type into a list, default threads per core to 1, and derive vCPUs. All requested facts are returned when the device list is empty as well.

Validation: `python -m pytest test/units/module_utils/facts/hardware` passed (15 tests). `ansible-test units test/units/module_utils/facts/hardware` could not match that path as a target pattern. `git diff --check` passed.
