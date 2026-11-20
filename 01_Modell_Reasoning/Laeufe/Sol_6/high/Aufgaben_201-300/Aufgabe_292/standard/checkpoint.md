# Checkpoint

- Task: give filesystem storage pollers a cancellable lifecycle and expose safe store `Close` methods.
- Status: poller and five backends updated; Git, S3, and Azure remote operations now receive the poller context; lifecycle tests added; filesystem suite and targeted race tests passed offline.
