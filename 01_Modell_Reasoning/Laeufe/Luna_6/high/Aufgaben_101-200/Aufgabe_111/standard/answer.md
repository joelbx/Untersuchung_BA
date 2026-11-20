Amazon Linux detection now recognizes releases 2023, 2025, 2027, and 2029. `YYYY.MM` releases still normalize to `1`, and unrecognized releases return `unknown`, so `GetEOL` reports `found=false` for them.

Added standard support dates: 2023 → 2029-06-30, 2025 → 2031-06-30, 2027 → 2033-06-30, and 2029 → 2035-06-30. System release parsing now handles the newer Amazon Linux banners.

`go test ./config ./scanner` passed. Updates are in [config/os.go](/app/config/os.go) and [redhatbase.go](/app/scanner/redhatbase.go).