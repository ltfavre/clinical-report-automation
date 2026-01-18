"""Template rendering utilities for reports."""

from typing import Dict


def render_template(data: Dict[str, object]) -> str:
    """Render a simple plaintext report from `data`.

    Replace with a full templating solution (Jinja2, Mako) as needed.
    """
    title = data.get("title", "Untitled Report")
    body = data.get("body", "(no content)")
    return f"{title}\n\n{body}\n"


def render_ser_p2_from_slots(slots: Dict[str, object], client: Dict[str, object]) -> str:
    """Render a simple SER P2-style markdown report from `slots` and `client`.

    This is a minimal synthetic renderer for demo and examples. Replace with
    a proper templating system (Jinja2) for production use.
    """
    title = f"Client {client.get('client_id', 'Unknown')} - Clinical Report"
    lines = [f"# {title}", ""]
    lines.append(f"**Age:** {client.get('age', 'N/A')}  ")
    lines.append(f"**Gender identity:** {client.get('gender_identity', 'N/A')}  ")
    lines.append("")

    concerns = client.get("presenting_concerns") or []
    if concerns:
        lines.append("## Presenting Concerns")
        for c in concerns:
            lines.append(f"- {c}")
        lines.append("")

    s1 = slots.get("s1_text") or slots.get("s1") or ""
    if s1:
        lines.append("## Session 1 Notes")
        lines.append(s1.strip())
        lines.append("")

    return "\n".join(lines)
