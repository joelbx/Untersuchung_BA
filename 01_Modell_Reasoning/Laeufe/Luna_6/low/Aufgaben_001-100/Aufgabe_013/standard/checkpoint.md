# Checkpoint

Issue: Fix ansible-doc terminal macro rendering, preserving ordinary parenthesized text and rendering multiple supported tokens in sequence.

Plan: Inspect `DocCLI.tty_ify` and its tests, implement the public transformation, then run the relevant existing tests.
