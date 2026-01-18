"""Data validation helpers for report automation."""

from typing import Dict


def validate_data(data: Dict[str, object]) -> bool:
    """Validate extracted `data` for required fields.

    Raises `TypeError` or `ValueError` on invalid input. Returns True when valid.
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dict")
    if "title" not in data:
        raise ValueError("missing required field: title")
    return True
