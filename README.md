# AI Insurance Underwriting Assistant (Claude-powered)

## Problem
Commercial underwriting is:
- time-consuming
- inconsistent
- prone to human bias

## Solution
This tool uses **Claude AI** to:
- Analyze risk submissions
- Generate underwriting summaries
- Suggest pricing & risk flags

## Features
- Risk scoring (Low / Medium / High)
- Key exposure identification
- Suggested underwriting actions
- Summary report generation

## Tech Stack
- Claude API (Anthropic)
- Python
- JSON input

## Example Input
```json
{
  "industry": "Warehouse",
  "location": "Dubai",
  "sum_insured": 5000000,
  "construction": "Non-combustible",
  "fire_protection": "Sprinkler"
}
```

## Example Output
- Risk Level: Medium
- Key Concerns: Fire load, storage type
- Suggested Rate: X%

## Why Claude?
Claude excels at:
- Long context understanding
- Structured reasoning
- Safer decision outputs

## Future Improvements
- Integration with MT5 trading signals
- Portfolio-level risk analytics
- Automation workflows (e.g., n8n)

## Author
JPFunRide
