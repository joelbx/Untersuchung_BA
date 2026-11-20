# EC2 availability check

Task: make EC2 detection validate the instance ID returned by IMDS, add functional client options and IMDS client injection, and run the existing relevant tests.

Status: implemented and verified. `go test ./lib/utils -count=1` and `go test ./lib/labels/ec2 -count=1` pass. The focused availability tests also pass. The EC2 hostname/label integration tests cannot build in this checkout because the system lacks `linux/hidraw.h` and the SQLite C dependency fails to compile.
