# Engineering standards

Apply these rules when reviewing changes to this sample.

1. Retry only `TransientError`. Validation errors and permanent failures must be returned to the caller immediately; do not hide them in retry loops.
2. Every transport request must pass an explicit positive timeout no greater than ten seconds. Do not rely on an implicit transport default.
3. Never log a credential value. Boolean presence indicators and a fixed `[redacted]` marker are allowed.

Check implementation against the public contracts in README.md. Avoid style-only findings.
