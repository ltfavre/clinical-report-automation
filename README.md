# Clinical Report Automation

Lightweight pipeline for generating synthetic clinical reports from structured inputs and session text.

## Quickstart (PowerShell)

From the repository root run the demo with `src` on `PYTHONPATH` so the package imports work:

```powershell
# from project root
$env:PYTHONPATH = "$PWD\src"
python .\examples\run_demo.py
```

The demo writes a Markdown report to `examples/sample_output/generated_report.md`.

## Files

- `src/report_automation/`: core package modules (`pipeline.py`, `templates.py`, `extractors.py`, `validators.py`, `exporters.py`).
- `examples/`: demo inputs and runner.
  - `examples/sample_inputs/` contains synthetic `intake.json` and `s1_text.txt`.
  - `examples/run_demo.py` generates `examples/sample_output/generated_report.md`.

## Notes

- This repo contains minimal placeholder implementations intended for portfolio/demo purposes; replace the renderer and exporters with production-ready templating (e.g., Jinja2) and PDF/Word exporters as needed.
- If you prefer not to set `PYTHONPATH`, run the demo from a virtualenv where `src/` is installed as a package (add packaging metadata first).

## License

Add a license if you wish (e.g., MIT).