# Checkpoint

Task: update affiliate queue identifier class for ISBN and ASIN, equality, and serialization.

Status: investigating root cause and callers before editing implementation.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep`/`find` fallback.

Investigation: baseline affiliate tests pass (16 tests). The dataclass is named PrioritizedISBN and has only `isbn`, `priority`, `timestamp`; generated equality compares priority/timestamp while identifier is excluded. Its default hash is unavailable because the dataclass is mutable. Submit compares a string to queue objects, so duplicate detection always misses. The lookup worker extracts `.isbn` and `process_amazon_batch` stages every returned product. Vendor serialization supplies `source_records: ['amazon:<ASIN>']`, usable to apply per-identifier staging.

Hypothesis: making identifier the equality/hash key, using queue objects for duplicate checks, and passing stage intent to the batch processor will solve deduplication and conditional staging. Preserve old class/constructor as compatibility wrapper.

Implementation: introduced PrioritizedIdentifier with identifier, stage_import, identifier-only equality/hash, and JSON-compatible serialization. Retained PrioritizedISBN constructor/property wrapper. Queue consumers and Submit use identifier-aware items. Batch processing caches all returned products and stages only those requested, matching Amazon source ASIN or ISBN-13. A later normal Submit enables staging on an already queued lookup-only item.

Reproduction: newly added tests initially failed because PrioritizedIdentifier did not exist; isolated staging test then failed for ISBN-13 matching; duplicate submission test failed when staging remained false. These failures were resolved by the final changes.

Verification: `python -m pytest -q scripts/tests/test_affiliate_server.py` passed (19 tests); `ruff check scripts/affiliate_server.py scripts/tests/test_affiliate_server.py` passed; `git diff --check` passed. Ruff emitted only its existing pyproject deprecation warning.
