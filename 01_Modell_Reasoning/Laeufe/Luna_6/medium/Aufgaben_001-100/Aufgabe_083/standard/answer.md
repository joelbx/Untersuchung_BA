Updated the XAttr helpers to use `XAttrCreateParams`, added `DeepPartial` and typed parsing, omitted zero block remainders and absent digests, and normalized lowercase `sha1` during parsing. Updated the upload worker and relevant tests.

The focused test suite passes, and `yarn workspace proton-drive check-types --pretty false` completes successfully.