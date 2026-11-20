Updated the OSS migration to **downgrade the existing `admin` role in place** and keep users and trusted-cluster mappings on `admin`. It also repairs `ossuser` assignments left by the earlier migration, and legacy user creation now assigns `admin`.

The migration, role, and `tctl` package tests passed.