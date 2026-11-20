The issue spans four points in the output path:

- [Display.display](/app/lib/ansible/utils/display.py:244) writes and flushes `stdout` or `stderr` directly. It has no parent thread lock or worker queue proxy.
- [FinalQueue](/app/lib/ansible/executor/task_queue_manager.py:61) already transports results and callbacks. It is the likely home for `DisplaySend` and `send_display`.
- [WorkerProcess._run](/app/lib/ansible/executor/process/worker.py:140) needs to set the display queue before worker display calls. [WorkerProcess.run](/app/lib/ansible/executor/process/worker.py:125) contains the late stream redirection workaround.
- [results_thread_main](/app/lib/ansible/plugins/strategy/__init__.py:113) needs to replay queued display calls before its sentinel ends processing. [TaskQueueManager.cleanup](/app/lib/ansible/executor/task_queue_manager.py:335) needs the requested stream flushes.

The fix should preserve every positional and keyword argument to `Display.display`, serialize parent writes, and drain worker display events before shutdown. Existing display tests cover only a basic parent write; the strategy unit test module is skipped, so they do not establish those concurrency or shutdown behaviors.

I recorded the diagnosis in `.codex-role-output/checkpoint.md`. I did **not** edit project source or tests: the active specialist instruction permits fault localization only, despite the request to implement the fix.