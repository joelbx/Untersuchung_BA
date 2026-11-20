Implemented the XAttr refactor: added `DeepPartial` and exported types, moved file metadata into `XAttrCreateParams`, updated the upload caller, and made parsing return a neutral structure for malformed or partial input. Creation now omits zero remainders and absent digests, and normalizes SHA1 keys.

The encryption helper takes the metadata object while retaining its required key arguments.

Verification passed: the focused XAttr Jest suite, Drive strict type check, and `git diff --check`.