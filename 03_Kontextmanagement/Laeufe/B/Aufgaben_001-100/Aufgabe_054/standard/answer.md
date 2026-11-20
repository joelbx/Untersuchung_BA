Implemented generic `GetInstance` in [singleton.go](/app/utils/singleton/singleton.go). It returns the concrete type, keeps `T` and `*T` separate, and runs each type’s constructor once under concurrent calls.

The singleton tests pass, including 20,000 concurrent calls and the race detector.