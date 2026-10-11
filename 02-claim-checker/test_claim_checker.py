import unittest

from claim_checker import check_claims


FACTS = {
    "capital of Nigeria": "Abuja",
    "largest city in Nigeria": "Lagos",
    "currency of Ghana": "cedi",
}


class ClaimCheckerTests(unittest.TestCase):
    def status_of(self, verdicts, key):
        return next(v.status for v in verdicts if v.key == key)

    def test_correct_claim_is_supported(self):
        text = "The capital of Nigeria is Abuja. It sits in the centre of the country."
        verdicts = check_claims(text, FACTS)
        self.assertEqual(self.status_of(verdicts, "capital of Nigeria"), "supported")

    def test_wrong_claim_is_contradicted(self):
        text = "The capital of Nigeria is Lagos."
        verdicts = check_claims(text, FACTS)
        self.assertEqual(self.status_of(verdicts, "capital of Nigeria"), "contradicted")

    def test_missing_topic_is_unverifiable(self):
        verdicts = check_claims("Ghana is in West Africa.", FACTS)
        self.assertEqual(self.status_of(verdicts, "capital of Nigeria"), "unverifiable")

    def test_matching_is_case_insensitive(self):
        verdicts = check_claims("the CAPITAL OF NIGERIA IS abuja.", FACTS)
        self.assertEqual(self.status_of(verdicts, "capital of Nigeria"), "supported")

    def test_one_response_can_support_and_contradict(self):
        text = "The capital of Nigeria is Abuja. The largest city in Nigeria is Abuja."
        verdicts = check_claims(text, FACTS)
        self.assertEqual(self.status_of(verdicts, "capital of Nigeria"), "supported")
        self.assertEqual(self.status_of(verdicts, "largest city in Nigeria"), "contradicted")


if __name__ == "__main__":
    unittest.main()
