Task complete: collection install --upgrade/-U implemented and forwarded through install_collections to dependency resolution.
Behavior: requested collections choose newest allowed release; installed compatible dependencies remain preferred; incompatible dependencies resolve to allowed releases; prereleases require --pre or an explicit pin; repeat upgrades skip reinstalling unchanged versions; requirements-file requests use the same path.
Coverage: unit tests for selection, constraints, prereleases, dependency preference, and idempotency; integration upgrade.yml for CLI, requirements, no-deps, and impossible constraints.
Validation: 61 relevant unit tests passed; upgrade.yml parsed as YAML; git diff --check passed. Pulp-backed integration tests were not run locally.
