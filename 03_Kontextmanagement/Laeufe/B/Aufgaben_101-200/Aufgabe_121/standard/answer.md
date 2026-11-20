Implemented `flipt.is_auth_method(input, name)` and registered it for both authorization engines. It maps the seven supported names to the `auth.proto` method codes, including the `k8s` alias, and returns the specified errors for missing authentication and unsupported names.

Tests for matches, mismatches, errors, argument types, and arity passed, along with the existing engine tests.