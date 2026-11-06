"""Small export adapter for a synthetic partner integration."""

from .service import list_page


def export_page(items, offset, batch_size):
    """Return one export page using a positive requested batch size."""
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")
    return list_page(items, offset, batch_size)


def export_snapshot(items, batch_size):
    """Return the first batch for a catalog snapshot export."""
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")
    page, next_offset = list_page(items, 0, batch_size)
    return {"items": page, "next_offset": next_offset}
