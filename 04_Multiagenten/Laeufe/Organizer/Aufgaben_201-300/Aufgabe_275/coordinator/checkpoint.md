Task: Correct Kubernetes proxy authentication error classification and provide the named httplib error-writer interfaces.
Status: Complete. authenticate now wraps non-access authorization/setup errors, preserving trace classification. Added httplib wrappers with custom ErrorWriter and retained existing default wrappers. Updated proxy classification tests and added wrapper tests.
Verification: go test ./lib/kube/proxy ./lib/httplib passed; git diff --check passed.
Delegation: none.
