# Checkpoint

Issue: propagate owner-encrypted session keys through entity loaders and cache so mail detail entities decrypt before use.

Initial inspection: repository at `/app`; locating loaders, mail detail call sites, and existing tests. `rg` is unavailable, using filesystem/search alternatives.
