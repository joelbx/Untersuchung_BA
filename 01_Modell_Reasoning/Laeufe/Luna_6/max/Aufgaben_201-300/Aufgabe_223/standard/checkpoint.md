# Checkpoint

## Objective
Resolve Python module shebang handling while preserving module-declared interpreters and arguments, honoring explicit overrides, and using a default only when a module has no shebang.

## Completed
- Added shebang extraction with `shlex.split` and made shebang resolution always return a complete line and interpreter.
- New-style Python wrappers now derive their shebang from the module source, including interpreter arguments; configured Python overrides still take precedence.
- `modify_module` only rewrites an existing shebang when its resolved interpreter differs, inserts the encoding line after shebangs, and supplies the default for modules without a shebang.
- Targeted existing module-common, interpreter-discovery, and action unit tests pass (61 passed).
