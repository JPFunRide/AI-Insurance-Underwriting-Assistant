import anthropic
import os


def analyze_risk(data: dict) -> str:
    """Analyze an insurance risk submission using Claude and return structured advice."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=api_key)
    prompt = f"""
    Analyze this insurance risk submission:
    {data}

    Provide:
    - Risk Level
    - Key Risks
    - Underwriting Recommendation
    """
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content


if __name__ == "__main__":
    # Example usage
    sample_data = {
        "industry": "Warehouse",
        "location": "Dubai",
        "sum_insured": 5000000,
        "construction": "Non-combustible",
        "fire_protection": "Sprinkler"
    }
    result = analyze_risk(sample_data)
    print(result)
