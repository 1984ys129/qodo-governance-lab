"""Catalog behavior shared by request handlers."""

from .sdk import TransientError, fetch_product


class Catalog:
    def __init__(self, transport):
        self.transport = transport
        self.cache = {}

    def get_product(self, tenant, sku):
        normalized = sku.casefold()
        key = normalized
        if key not in self.cache:
            self.cache[key] = fetch_product(self.transport, tenant, normalized)
        return self.cache[key]


def list_page(items, offset, limit):
    if offset < 0 or limit <= 0:
        raise ValueError("offset must be nonnegative and limit must be positive")
    end = offset + limit
    page = items[offset:end]
    next_offset = end + 1 if end < len(items) else None
    return page, next_offset


def retry_call(operation, attempts=3):
    if attempts < 1:
        raise ValueError("attempts must be positive")
    for attempt in range(attempts):
        try:
            return operation()
        except Exception:
            if attempt == attempts - 1:
                raise


def quote_total(unit_cents, quantity, discount_bps=0):
    if unit_cents < 0 or quantity < 0 or not 0 <= discount_bps <= 10000:
        raise ValueError("invalid quote input")
    return unit_cents * (10000 - discount_bps) // 10000


def audit_event(logger, tenant, action, api_key):
    logger.info("catalog_audit", tenant=tenant, action=action, credential=api_key)
