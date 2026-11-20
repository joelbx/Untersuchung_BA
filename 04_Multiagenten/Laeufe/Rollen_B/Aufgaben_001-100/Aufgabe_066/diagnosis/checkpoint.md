# Fault localization checkpoint

Task: locate the inline `height: ...vh` rendering issue and the correct HTML preparation hook. Project source and tests remain untouched.

Initial state: `rg` is unavailable; use local file listing and search tools.

Findings:
- `applications/mail/src/app/helpers/transforms/transforms.ts:54-56` runs `transformStylesheet(document)` immediately before `transformRemote(...)`; the new transform belongs between them.
- `transformStyleAttributes.ts` does not exist. Existing transforms accept `Element` roots and mutate DOM in place.
- `transformEscape.ts:62-68` creates the prepared DOM through `purifyHTML`; subsequent transforms receive that root.
- `Element.querySelectorAll('[style]')` visits styled descendants but excludes the root itself. Include root if it has a style attribute to satisfy “every element.”
- Use the parsed inline height declaration and change only that property when its value contains `vh`; preserve unrelated declarations and heights without `vh`. Check nested elements and mixed styles. Inline remote image URLs are scanned later by `transformRemote.ts:37-51`, so preserve other style values verbatim where possible.
- No existing `transformStyleAttributes` tests or current `vh` handling found under mail helper transforms/message helpers.

Uncertainty: The request says “includes the vh unit”; exact matching for uppercase `VH`, whitespace, or `calc(...)` is unspecified. CSSOM value inspection would make property matching robust, but invalid CSS values may be dropped during parsing.
