# Checkpoint

Task: route `Display.display` calls from forked workers to the parent through the final results queue, serialize parent display writes with a lock, and flush standard streams during task queue manager cleanup.

Status: implementation complete. Workers now forward display events through `FinalQueue`; the strategy result thread dispatches them in the parent; worker shutdown no longer redirects stdout/stderr; manager cleanup flushes both streams.

Verification: focused display, TQM callback, and linear strategy tests passed. Warning display tests passed individually. A combined run showed shared-singleton warning deduplication and a linear test fixture type error; the linear test passed when run alone. `git diff --check` passes.
