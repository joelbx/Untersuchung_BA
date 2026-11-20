# Fault-localization progress

Inspected `lib/ansible/cli/doc.py`, shared `CLI.tty_ify` in `lib/ansible/cli/__init__.py`, and existing CLI tests. No project source or tests changed.

`DocCLI` has no `tty_ify` override, so calls throughout its display paths inherit `CLI.tty_ify` (`lib/ansible/cli/__init__.py:449`). That method substitutes only I, B, M, U, and C. Its patterns at lines 54-58 lack a preceding word boundary, so the M in `IBM(...)` matches and produces `IB[...]`. No substitution handles L, R, or HORIZONTALLINE. A direct call to `DocCLI.tty_ify` confirmed all reported failures, including a mixed-macro line retaining `R(text,ref)` verbatim. Existing CLI unit/integration tests found no direct `tty_ify` coverage.

Likely fix location: a `DocCLI.tty_ify(text)` implementation in `lib/ansible/cli/doc.py` (the requested public entry point), covering I/B/M/U/C, L/R with optional post-comma space, HORIZONTALLINE, repeated macros in one line, and preservation of ordinary parenthesized words. Scope uncertainty: wider CLI callers of inherited `CLI.tty_ify` may retain the old behavior if only DocCLI is changed; the reported requirements address ansible-doc.
