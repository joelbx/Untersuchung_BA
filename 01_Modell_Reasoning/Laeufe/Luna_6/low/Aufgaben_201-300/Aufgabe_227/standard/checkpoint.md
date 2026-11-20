# Checkpoint

Issue: restrict the MIME suffix workaround version gate to runtime Qt only, with explicitly documented `compiled` semantics and rejection of `compiled=True, exact=True`.

Plan: locate the compatibility helper and MIME suffix handling, update implementation and existing tests as needed, then run the relevant existing tests.
