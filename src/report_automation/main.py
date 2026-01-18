"""Simple report generation placeholders."""

from typing import Any, Dict


def generate_report(data: Dict[str, Any]) -> str:
    """Generate a simple placeholder report from `data`.

    Replace this with real report-building logic.
    """
    title = data.get("title", "Untitled Report")
    return f"Report: {title}\n(placeholder)"


if __name__ == "__main__":
    sample = {"title": "Sample Clinical Report"}
    print(generate_report(sample))
