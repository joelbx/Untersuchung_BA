# Checkpoint

Implemented `packages/shared/lib/eventManager/polling.ts` with exported `interval` and `maxPollingSteps` constants and `pollEvents`.

The helper subscribes only when both a property and action are provided, runs at most five calls with 5000 ms delays, stops and unsubscribes on a matching array item, and cleans up on completion or error. Type validation passed with `yarn workspace @proton/shared check-types`.
