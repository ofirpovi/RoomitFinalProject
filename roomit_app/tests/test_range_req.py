import unittest
from ..requirements.RangReq import RangeReq


class TestRangeReq(unittest.TestCase):
    def test_calculate_score_when_min_and_max_are_none(self):
        req = RangeReq([], 1, "Test", None, None)

        score = req.calculate_score(42)

        self.assertEqual(score, 1)

    def test_calculate_score_when_max_is_none(self):
        req = RangeReq([], 1, "Test", 10, None)

        score1 = req.calculate_score(5)
        score2 = req.calculate_score(15)

        self.assertEqual(score1, 0)
        self.assertEqual(score2, 1)

    def test_calculate_score_when_answer_is_none(self):
        # Arrange
        req = RangeReq([], 1, "Test", 10, 20)

        # Act
        score = req.calculate_score(None)

        self.assertEqual(score, 0)

    def test_calculate_score_when_answer_is_not_an_int(self):
        req = RangeReq([], 1, "Test", 10, 20)

        with self.assertRaises(TypeError):
            req.calculate_score("not a number")

    def test_calculate_score_when_answer_is_within_range(self):
        req = RangeReq([], 1, "Test", 10, 20)

        score = req.calculate_score(15)

        self.assertEqual(score, 1)

    def test_calculate_score_when_answer_is_outside_range_but_within_tolerance(self):
        req = RangeReq([], 1, "Test", 10, 20)

        score = req.calculate_score(23)

        self.assertAlmostEqual(score, 0.92, delta=0.4)

    def test_calculate_score_when_answer_is_outside_range_and_outside_tolerance(self):
        req = RangeReq([], 1, "Test", 10, 20)

        score = req.calculate_score(35)

        self.assertEqual(score, 0)

    def test_both_min_max_none(self):
        requirement = RangeReq([], 10, "Test requirement", None, None)
        score = requirement.calculate_score(50)
        self.assertEqual(score, 10)

    def test_answer_not_int(self):
        requirement = RangeReq([], 10, "Test requirement", 0, 100)
        with self.assertRaises(TypeError):
            requirement.calculate_score("not an int")

    def test_answer_outside_range(self):
        requirement = RangeReq([], 1, "Test requirement", 0, 100)
        score = requirement.calculate_score(-10)
        self.assertAlmostEqual(score, 0.94, delta=0.5)

        score = requirement.calculate_score(200)
        self.assertAlmostEqual(score, 0.85, delta=0.5)

    def test_answer_equal_to_min_max(self):
        requirement = RangeReq([], 10, "Test requirement", 0, 100)
        score = requirement.calculate_score(0)
        self.assertEqual(score, 10)

        score = requirement.calculate_score(100)
        self.assertEqual(score, 10)


if __name__ == '__main__':
    unittest.main()
