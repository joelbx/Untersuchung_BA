Updated `authenticate` to preserve non-access errors from authorization and context setup while returning `AccessDenied` for access-related failures. Expanded `TestAuthenticate` to check the classification of each reported case.

The focused test and the full `lib/kube/proxy` test suite pass.