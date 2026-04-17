"""Main entry point for the AI Insurance Underwriting Assistant.

This module provides a command-line interface to process insurance risk
submissions, generate a preliminary underwriting summary using internal
risk rules, build a prompt for Claude using a template, and call Claude
via the ClaudeClient wrapper. The response from Claude is then printed
for the user.

Run this script from the command line and provide a path to a JSON file
containing the risk submission data.
"""

import argparse
import json
from pathlib import Path

# Import local modules
from claude_client import claude_client
from risk_rules import generate_underwriting_summary

# Path to the prompt template (stored in the prompts folder)
PROMPT_TEMPLATE_PATH = Path("prompts/underwriting_prompt.txt")


def load_prompt_template() -> str:
    """Load the prompt template from file."""
    with open(PROMPT_TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return f.read()


def build_claude_prompt(data: dict, summary: tuple[str, list[str]]) -> str:
    """Construct the prompt text to send to Claude.

    Args:
        data (dict): Risk submission data.
        summary (tuple): Tuple of (risk_level, recommendations).

    Returns:
        str: A prompt string ready for Claude.
    """
    risk_level, recommendations = summary
    rec_text = "\n".join(f"- {rec}" for rec in recommendations) if recommendations else "None"

    template = load_prompt_template()
    # Inject dynamic values into the template
    prompt = template.format(
        data=json.dumps(data, indent=2),
        risk_level=risk_level,
        recommendations=rec_text,
    )
    return prompt


def process_submission(file_path: Path) -> None:
    """Process a single risk submission JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Generate preliminary summary using internal rules
    summary = generate_underwriting_summary(data)

    # Build prompt for Claude
    prompt = build_claude_prompt(data, summary)

    # Call Claude
    response = claude_client.call_claude(prompt)

    # Print results
    print("Underwriting Summary (Internal Rules):")
    print(f"Risk Level: {summary[0]}")
    print("Recommendations:")
    for rec in summary[1]:
        print(f"  - {rec}")
    print("\nClaude Response:\n")
    print(response)


def main():
    parser = argparse.ArgumentParser(description="Analyze an insurance risk submission using Claude.")
    parser.add_argument("input", type=Path, help="Path to the JSON file containing the risk submission.")
    args = parser.parse_args()

    process_submission(args.input)


if __name__ == "__main__":
    main()
