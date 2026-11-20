Task: implement collection install --upgrade with constraint-aware dependency resolution and opt-in prereleases.
Status: implemented CLI flag, upgrade-aware candidate selection, idempotent install skipping, and no-deps constraint validation. Added unit coverage and upgrade.yml integration tasks.
Verification: 145 relevant unit tests pass with ANSIBLE_DEVEL_WARNING=False; integration YAML parses. Container-backed integration target was not run.
