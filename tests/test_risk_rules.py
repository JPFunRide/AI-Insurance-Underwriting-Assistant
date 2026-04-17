import unittest

from risk_rules import validate_submission, calculate_hazard_score, classify_risk_level, generate_underwriting_summary


class TestRiskRules(unittest.TestCase):
    def setUp(self):
        # Sample complete risk submission
        self.complete_data = {
            "industry": "warehouse",
            "location": "Dubai",
            "sum_insured": 1000000,
            "construction": "non-combustible",
            "fire_protection": "sprinkler"
        }
        # Sample incomplete risk submission (missing industry)
        self.incomplete_data = {
            "location": "Dubai",
            "sum_insured": 1000000,
            "construction": "non-combustible",
            "fire_protection": "sprinkler"
        }

    def test_validate_submission_complete(self):
        missing = validate_submission(self.complete_data)
        self.assertEqual(missing, [])

    def test_validate_submission_missing(self):
        missing = validate_submission(self.incomplete_data)
        self.assertIn("industry", missing)

    def test_hazard_score_and_classification(self):
        score = calculate_hazard_score(self.complete_data)
        # Score should be an integer and positive in this example
        self.assertIsInstance(score, int)
        self.assertGreaterEqual(score, 0)
        level = classify_risk_level(score)
        self.assertIn(level, ["Low", "Medium", "High"])

    def test_generate_underwriting_summary(self):
        risk_level, recommendations = generate_underwriting_summary(self.complete_data)
        self.assertIsInstance(risk_level, str)
        self.assertIsInstance(recommendations, list)


if __name__ == "__main__":
    unittest.main()
