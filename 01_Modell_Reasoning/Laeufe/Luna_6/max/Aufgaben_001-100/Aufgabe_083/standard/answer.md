Implemented the XAttr refactor: added `DeepPartial`, typed the metadata options and parsed shapes, froze created attributes, omitted zero remainders and absent digests, and hardened parsing with SHA1 key normalization. Updated the upload worker and exported the new types.

Validation passed: focused XAttr Jest suite, Drive TypeScript check, Prettier check, and `git diff --check`.

Key files: [extendedAttributes.ts](/app/applications/drive/src/app/store/_links/extendedAttributes.ts), [DeepPartial.ts](/app/applications/drive/src/app/utils/type/DeepPartial.ts).