Task: Refactor drive extended attributes to object parameters, strict types, and tolerant parsing.
Status: complete. Targeted XAttr tests pass (5/5); Drive TypeScript check passes; git diff --check passes.
Files: store/_links/extendedAttributes.ts, store/_links/extendedAttributes.test.ts, store/_uploads/worker/worker.ts, services/extendedAttributes.ts, utils/type/DeepPartial.ts.
