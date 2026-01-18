"""Simple demo script to generate a report from the `examples/sample_inputs` files."""

from report_automation.pipeline import generate_report

fake_slots = {
	"conversation_initiation": "Finds initiating conversations difficult",
	"expressive_communication": "Tends to overexplain and be overly direct",
	"receptive_communication": "May miss sarcasm or implied meaning",
	"conversation_flow": "Occasionally interrupts when anxious"
}

fake_client = {
	"id": "A001",
	"age": 32
}

report_text = generate_report(fake_slots, fake_client)

with open("examples/sample_output/generated_report.md", "w", encoding="utf-8") as f:
	f.write(report_text)

print("Demo report generated → examples/sample_output/generated_report.md")

