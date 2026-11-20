Implemented `removeTechnicalFields` in [EntityUtils.ts](/app/src/api/common/utils/EntityUtils.ts:134). It mutates entities recursively, removing keys with the specified prefixes while preserving other fields. Added coverage for root and nested fields, arrays, and entities without technical fields.

Validation passed: `npm run types` and `npm run fasttest` (8,685 assertions).