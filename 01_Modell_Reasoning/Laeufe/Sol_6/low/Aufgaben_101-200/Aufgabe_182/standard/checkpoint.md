Task: Route worker Display calls through the main process with method context and exact caller arguments.
Status: Implemented proxy_display for display, warning, deprecated; DisplaySend carries method; results thread dispatches by method. Updated and added focused unit tests.
Verification: PYTHONPATH=lib python -m pytest -q test/units/utils/test_display.py test/units/utils/display/test_display.py test/units/executor/test_task_queue_manager_callbacks.py test/units/plugins/strategy/test_strategy.py — 17 passed, 7 skipped.
