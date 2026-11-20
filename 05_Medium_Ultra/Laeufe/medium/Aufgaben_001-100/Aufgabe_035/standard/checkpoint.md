# Checkpoint

Task: decouple flag evaluation from RuleStore.
Status: implemented storage.Evaluator and EvaluatorStorage; Server delegates to it. Evaluation preserves rule rank, normalizes operators and string whitespace, and uses inclusive CRC32 rollout cutoffs. Existing storage/server tests plus focused evaluator tests pass.
