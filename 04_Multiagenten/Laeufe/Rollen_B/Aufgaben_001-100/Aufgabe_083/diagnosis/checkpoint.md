# Fault-localization progress

Inspected `applications/drive/src/app/store/_links/extendedAttributes.ts`, its existing tests, and the upload caller. The issue's `services/extendedAttributes.ts` and `utils/type/` paths do not exist in this checkout; the implementation is under `store/_links/`.

Findings: file creation and encryption use positional arguments; the upload worker and tests call that signature. File creation always appends a remainder, producing a trailing zero for exact chunk multiples and `[0]` for an empty file. Both attribute interfaces allow a present digest object without a SHA1 string. Parse helpers use `any`; `parseMedia` and `parseDigests` dereference JSON `null` and can throw. Existing tests cover ordinary partial data and malformed JSON, but omit null nested objects, exact chunk boundaries, and strict type contracts.

Fix coverage to recommend: object parameters and migrated caller/tests; exported `DeepPartial`/`MaybeExtendedAttributes`; required canonical digest values when present; conditional remainder; ISO creation and seconds parsing; neutral partial output on malformed input including null nested objects; media/digest normalization.

Uncertainty: requirement says encryption takes the params object as its sole parameter, while its interface also lists two key parameters. Existing call and encryption helper need both keys, so likely only file metadata should collapse into the first object while keys remain arguments, unless the intended API explicitly moves keys into the object.
