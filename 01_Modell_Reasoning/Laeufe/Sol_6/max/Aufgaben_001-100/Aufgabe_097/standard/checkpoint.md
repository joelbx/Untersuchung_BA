# Controller Python minimum update

Status: implementation complete; focused verification passed on the available Python 3.11 interpreter.

The issue requests a coordinated controller minimum update. Its explicit acceptance requirement is Python 3.12 or newer; implementation will use 3.12 consistently and preserve compatibility for managed nodes where separately supported.

Changed: CLI and ansible-test controller gates and messages, package metadata, ansible-test version lists, collection TarFile extraction, obsolete controller compatibility branches, unit dependency markers, and a public changelog fragment.

Verification: collection extraction (3 passed), collection loader (70 passed, 1 skipped), collection tar operations (7 passed), collection installation (6 passed), and role installation (7 passed). CLI and ansible-test reject Python 3.11 with identical error text. Tests requiring CLI imports were run after temporarily preloading that module with a simulated 3.12 version tuple; the runtime was still Python 3.11. A genuine Python 3.12 run is unavailable in this container.

The Azure CI matrix still lists 3.10 and 3.11 jobs; its harness configuration was left untouched under the task constraint.
