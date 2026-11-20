Implemented `removeTechnicalFields` in [EntityUtils.ts](/app/src/api/common/utils/EntityUtils.ts:134). It recursively removes the specified technical field prefixes from an entity and nested objects, including objects in arrays, while preserving other fields.

Validation passed: `npm run types` and `npm run fasttest` (8,676 assertions).