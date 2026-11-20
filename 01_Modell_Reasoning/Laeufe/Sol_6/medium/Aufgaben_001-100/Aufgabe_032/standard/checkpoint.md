Task: make async_wrapper exit output and job records consistent and atomic.
Status: implemented centralized JSON exits, atomic job writes, consistent lifecycle/error fields, timeout PID context, and cleanup policy reporting. Added focused tests for writes, errors, and timeouts. All 7 async_wrapper unit tests pass; git diff --check passes.
Constraints: edit checked-out files only; run relevant existing tests.
