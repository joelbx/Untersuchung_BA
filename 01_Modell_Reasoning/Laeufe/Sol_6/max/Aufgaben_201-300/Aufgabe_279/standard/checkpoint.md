# Payment token verification refactor

Status: verification refactor complete. Six call sites bind the default verifier (the five requested components plus single signup). Polling reports status and releases its timer, listeners, and tab on settlement. Components and account TypeScript checks pass. Helper, modal, subscription, edit card, and account PaymentStep tests pass. Two CreditsModal assertions about PaymentMethodID fail against the existing chargeable-token result shape in HEAD; this is unrelated to the refactor.

Plan: extract injectable token verification and the default modal handler, update all five consumers, then run relevant existing tests.
