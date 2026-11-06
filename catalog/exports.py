"""Small export adapter for a synthetic partner integration."""

from .service import list_page


def export_page(items, offset, batch_size):
    """Return one export page using a positive requested batch size."""
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")
    return list_page(items, offset, batch_size)
