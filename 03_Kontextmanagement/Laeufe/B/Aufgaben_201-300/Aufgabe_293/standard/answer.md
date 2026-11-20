The OCI storage configuration work item is complete. Repository validation now gives the required errors, and the bundle directory, authentication, and poll interval settings are parsed and passed to the backend. The `fs/oci` suite is registered in the build and CI matrices.

The focused Go tests and `git diff --check` passed. The Dagger integration suite was registered but not run locally.