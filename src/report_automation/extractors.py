"""Data extractors for clinical sources."""

from typing import Any, Dict


def extract_from_source(source: Any) -> Dict[str, Any]:
    """Extract a dictionary of report fields from `source`.

    This is a placeholder: if `source` is a dict it is returned as-is;
    otherwise the function attempts a best-effort conversion.
    """
    if isinstance(source, dict):
        return source

    # Best-effort conversions for common simple types
    if hasattr(source, "to_dict"):
        return source.to_dict()
    try:
        return dict(source)
    except Exception:
        return {"title": "Extracted Report", "body": str(source)}
