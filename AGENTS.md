# Engineering standards

Apply these rules when reviewing changes to this sample.

1. Every transport request must pass an explicit positive timeout no greater than seven seconds. Do not rely on an implicit transport default.
2. Never log a credential value. Boolean presence indicators and a fixed `[redacted]` marker are allowed.
3. Do not use `eval()` or `exec()` to parse catalog identifiers.

Check implementation against the public contracts in README.md. Avoid style-only findings.
