Implemented [`singleton.GetInstance[T](func() T) T`](/app/utils/singleton/singleton.go), with one constructor call per exact type and safe concurrent access. `T` and `*T` have separate instances. I also migrated the four production callers to the typed API and added a test that releases 20,000 callers together.

The singleton race test and tests for all affected packages passed.