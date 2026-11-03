# Governance review lab

A synthetic Python catalog service used to study code understanding and review rules.
All identifiers, tenants, credentials and business behavior are fictional. No external service is called.

Python 3.10+; standard library only.

```text
python -m unittest discover -s tests -v
```

Contracts:

- Products are cached separately for each tenant and normalized SKU.
- Pagination offsets identify the next unread item. Empty final pages have no next offset.
- Quotes apply quantity and a basis-point discount to integer cents, rounding down once on the total.
- Transport operations require a positive timeout of at most seven seconds.
- Audit events may record whether a credential exists, but must never record its value.

The transport and logger interfaces are supplied by callers, allowing deterministic local execution.

This sample is provided under the MIT License. It contains no real customer code or data.
