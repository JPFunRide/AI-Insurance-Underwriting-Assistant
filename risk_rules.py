"""Risk rules and logic for insurance underwriting.

This module defines helper functions to validate a risk submission, calculate
simple hazard scores based on input data, and determine a risk level (Low,
Medium, High). These functions can be extended with more sophisticated logic
and actuarial data as needed.
"""

from typing import Dict, List, Tuple


def validate_submission(data: Dict) -> List[str]:
    """Validate that required fields are present in the risk submission.

    Args:
        data (dict): The risk submission data.

    Returns:
        list[str]: A list of missing required field names. Empty if all fields are present.
    """
    required_fields = ["industry", "location", "sum_insured", "construction", "fire_protection"]
    missing = [field for field in required_fields if field not in data or not data[field]]
    return missing


def calculate_hazard_score(data: Dict) -> int:
    """Calculate a simple hazard score for the risk submission.

    The scoring system here is illustrative and can be refined. Higher scores
    correspond to higher risk.

    Args:
        data (dict): The risk submission data.

    Returns:
        int: A hazard score.
    """
    score = 0

    # Occupancy / industry factor
    industry = data.get("industry", "").lower()
    if industry in {"chemical", "manufacturing", "oil & gas"}:
        score += 3
    elif industry in {"warehouse", "retail"}:
        score += 2
    else:
        score += 1

    # Construction material factor
    construction = data.get("construction", "").lower()
    if construction in {"combustible", "partially-combustible"}:
        score += 3
    elif construction == "non-combustible":
        score += 0
    else:
        score += 1

    # Fire protection factor
    protection = data.get("fire_protection", "").lower()
    if protection == "none":
        score += 3
    elif protection == "sprinkler":
        score += 0
    else:
        score += 1

    # Sum insured factor
    sum_insured = data.get("sum_insured", 0)
    try:
        # attempt to parse if string
        sum_val = float(sum_insured)
    except (TypeError, ValueError):
        sum_val = 0
    if sum_val > 10000000:
        score += 3
    elif sum_val > 5000000:
        score += 2
    elif sum_val > 1000000:
        score += 1

    return score


def classify_risk_level(score: int) -> str:
    """Classify the risk into Low, Medium, or High based on the hazard score.

    Args:
        score (int): The hazard score.

    Returns:
        str: "Low", "Medium", or "High".
    """
    if score <= 3:
        return "Low"
    elif score <= 6:
        return "Medium"
    else:
        return "High"


def generate_underwriting_summary(data: Dict) -> Tuple[str, List[str]]:
    """Generate an underwriting summary using simple rules.

    Returns a tuple of (risk_level, recommendations).

    Args:
        data (dict): The risk submission data.

    Returns:
        tuple[str, list[str]]: Risk level and list of recommendations.
    """
    missing = validate_submission(data)
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

    score = calculate_hazard_score(data)
    risk_level = classify_risk_level(score)

    # Generate basic recommendations
    recommendations = []
    if risk_level == "High":
        recommendations.append("Consider decline or strict risk control measures.")
    if data.get("fire_protection", "").lower() != "sprinkler":
        recommendations.append("Upgrade fire protection to a sprinkler system.")
    if data.get("construction", "").lower() in {"combustible", "partially-combustible"}:
        recommendations.append("Improve construction materials or compartmentalize high-risk areas.")

    return risk_level, recommendations
