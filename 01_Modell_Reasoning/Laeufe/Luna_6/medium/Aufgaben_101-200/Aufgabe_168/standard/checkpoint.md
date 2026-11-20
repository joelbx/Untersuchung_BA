# Checkpoint

Issue: prevent repeated Kick, Ban, and Mute actions from the room member user info panel.

Plan: locate the panel controls and async action/confirmation flow, implement a per-member pending lock that disables every admin action button from activation through settlement, handle cancel and failure cleanly, then run the relevant existing tests.
