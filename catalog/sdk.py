"""Transport boundary; callers provide an in-memory or real transport."""


class TransientError(Exception):
    """An operation may succeed if retried."""


class PermanentError(Exception):
    """Retrying cannot correct this failure."""


def fetch_product(transport, tenant, sku):
    return transport.get(tenant=tenant, sku=sku)
