Replaced the expression walker with typed AST nodes for literals, variables, email extraction, regex replacement, and boolean regex matching. Parsing now validates variable shape, namespaces, function arguments, result kinds, and expression depth. I also updated trait and PAM interpolation to validate variables at evaluation time.

`go test ./lib/utils/parse -count=1` passes. Service and server tests could not build: the CGO build lacks `linux/hidraw.h`, and a CGO-disabled build fails in BPF and U2F dependencies. `git diff --check` passes.

No delegation was used.