Progress: fault localization complete; project source and tests untouched.

Evidence:
- lib/ansible/executor/process/worker.py:171 sets Display._final_q in the worker.
- lib/ansible/utils/display.py:340-355 proxies only display(), calling send_display(msg, ...) with synthesized default kwargs. warning() and deprecated() at 478-505 run their local dedup dictionaries before calling display(), so each fork makes its own decision.
- lib/ansible/executor/task_queue_manager.py:63-67 DisplaySend carries only args/kwargs; FinalQueue.send_display at 98-101 constructs it without method context. The issue calls this TaskQueueManager.send_display, but the method belongs to FinalQueue.
- lib/ansible/plugins/strategy/__init__.py:113-122 receives DisplaySend and always invokes display.display(), so the parent cannot run warning/deprecated dedup logic.
- test/units/utils/test_display.py:103-118 asserts the current send_display(msg, all default kwargs) form; this expectation conflicts with the requested exact caller args/kwargs behavior. No existing warning/deprecated proxy coverage found.
- Existing targeted tests: 2 passed (test_Display_display_fork, test_Display_display_lock_fork).

Likely fix behavior: decorate display, warning, deprecated with proxy_display; in workers call _final_q.send_display(method.__name__, *args, **kwargs) once, otherwise call original method. Add method to FinalQueue.send_display and DisplaySend; dispatch with getattr(display, result.method)(*result.args, **result.kwargs). Parent result thread serializes all fork messages through one Display singleton and its warning/deprecation dictionaries. Verify exact positional/keyword preservation, one send per call, and cross-worker dedup. Possible semantic edge: deprecated(..., removed=True) currently raises in worker, but moving full method execution to parent may shift that exception to result thread; investigate separately if that case is covered by intended scope.
