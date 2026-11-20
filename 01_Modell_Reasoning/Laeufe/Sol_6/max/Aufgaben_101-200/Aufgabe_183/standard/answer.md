Updated [Ubuntu lifecycle data](/app/config/os.go:114): 20.04 has extended support through April 1, 2030; 22.04 is recognized with standard support through April 1, 2027, and extended support through April 1, 2032. Added [regression cases](/app/config/os_test.go:222) for the support transitions.

`go test ./config ./models` and `go test ./scanner` pass.