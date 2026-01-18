"""Exporters for generated reports."""

from typing import Any


def export_report(report: str, output_path: str) -> None:
    """Export `report` string to `output_path`.

    This placeholder writes plaintext. Replace with PDF/Word exporters as needed.
    """
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
