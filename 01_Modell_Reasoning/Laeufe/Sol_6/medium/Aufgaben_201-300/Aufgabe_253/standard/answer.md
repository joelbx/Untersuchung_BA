`GUIProcess` now shows output from both streams while the process runs. At completion, it publishes a final message only for streams with output: stdout as info, followed by stderr as error.

The updated tests cover live output and final message order. All 42 `GuiProcess` tests pass.