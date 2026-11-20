Task: implement generic singleton.GetInstance[T](func() T).
Status: completed. Added per-type sync.Map entries with sync.Once; T and *T use distinct reflect.Type keys. Added value/pointer reuse tests and a 20,000-goroutine constructor-once test. GOPROXY=off go test ./utils/singleton and go test -race ./utils/singleton both pass.
