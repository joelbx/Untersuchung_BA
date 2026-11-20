Added `flipt.is_auth_method(input, method)` to the authorization policy engine. It maps all seven supported strings to the protobuf method codes, including `k8s` and `kubernetes`, and returns the specified errors for missing authentication and unsupported methods.

The targeted tests passed for the new built-in and both authorization engines.