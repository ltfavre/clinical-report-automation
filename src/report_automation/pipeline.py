"""Pipeline orchestration for report automation."""

from .extractors import extract_from_source
from .validators import validate_data
from .templates import render_template
from .exporters import export_report
from report_automation.templates import render_ser_p2_from_slots


def run_pipeline(source: object, output_path: str) -> str:
    """Run the full report pipeline.

    Steps:
    - extract data from `source`
    - validate the extracted data
    - render a report string
    - export the report to `output_path`

    Returns the `output_path` on success.
    """
    data = extract_from_source(source)
    validate_data(data)
    report = render_template(data)
    export_report(report, output_path)
    return output_path


def generate_report(slots: dict, client: dict) -> str:
    """Generate a report from `slots` and `client` using SER P2 template."""
    sections = []
    sections.append(render_ser_p2_from_slots(slots, client))
    return "\n\n".join(sections)
