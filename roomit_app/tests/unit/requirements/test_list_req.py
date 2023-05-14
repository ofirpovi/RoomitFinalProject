import unittest
from roomit_app.requirements.ListReq import ListReq


class ListReqTest(unittest.TestCase):

    def message(self, testCase, expected, result):
        return "\nTest case  -  " + testCase + "\nExpected result  -  " + expected + "\nActual Result  -  " + result

    def test_calculate_score_desired_answer_none(self):
        req = ListReq(disqualifies=False, weight=1, text="test", desired_answer=None)
        result = req.calculate_score([])
        expected = None
        message = self.message("Calculate score desired answer None", str(expected), str(result))
        self.assertEqual(result, expected, message)

    def test_calculate_score_answer_none(self):
        req = ListReq(disqualifies=False, weight=1, text="test", desired_answer=['A'])
        result = req.calculate_score(None)
        expected = 0.5
        message = self.message("Calculate score answer None", str(expected), str(result))
        self.assertEqual(result, expected, message)

    def test_calculate_score_desired_answer_is_disjoint(self):
        req = ListReq(disqualifies=False, weight=1, text="test", desired_answer=['A'])
        result = req.calculate_score(['B'])
        expected = 0
        message = self.message("Calculate score desired answer is disjoint", str(expected), str(result))
        self.assertEqual(result, expected, message)

    # def test_calculate_score_answer_is_disjoint(self):
    #     req = ListReq(disqualifies=False, weight=1, text="test", desired_answer=['A'])
    #     result = req.calculate_score(['B'])
    #     expected = 0
    #     message = self.message("Calculate score answer is disjoint", str(expected), str(result))
    #     self.assertEqual(result, expected, message)

    def test_calculate_score_answer_is_subset(self):
        req = ListReq(disqualifies=False, weight=1, text="test", desired_answer=['A'])
        result = req.calculate_score(['A', 'B'])
        expected = 1
        message = self.message("Calculate score answer is subset", str(expected), str(result))
        self.assertEqual(result, expected, message)

    def test_calculate_score_answer_is_superset(self):
        req = ListReq(disqualifies=False, weight=1, text="test", desired_answer=['A', 'B'])
        result = req.calculate_score(['A'])
        expected = 1
        message = self.message("Calculate score answer is superset", str(expected), str(result))
        self.assertEqual(result, expected, message)

    def test_calculate_score_desired_answer_is_empty(self):
        requirement = ListReq(False, 5, "test", set())
        score = requirement.calculate_score(None)
        self.assertEqual(score, 2.5)

    def test_calculate_score_answer_is_none(self):
        requirement = ListReq(False, 5, "test", {"A", "B", "C"})
        score = requirement.calculate_score(None)
        self.assertEqual(score, 2.5)

    def test_calculate_score_answer_does_not_intersect_desired_answer(self):
        requirement = ListReq(False, 5, "test", {"A", "B", "C"})
        score = requirement.calculate_score({"D", "E", "F"})
        self.assertEqual(score, 0)

    def test_calculate_score_answer_intersects_desired_answer(self):
        requirement = ListReq(False, 5, "test", {"A", "B", "C"})
        score = requirement.calculate_score({"C", "D", "E"})
        self.assertEqual(score, 5)

    def test_calculate_score_no_desired_answer(self):
        # Test calculate_score() with no desired answer
        requirement = ListReq([], 1, "text", None)
        self.assertIsNone(requirement.calculate_score(None))

    def test_calculate_score_desired_answer_dont_care(self):
        # Test calculate_score() with desired answer "D"
        requirement = ListReq([], 2, "text", "D")
        self.assertEqual(requirement.calculate_score([]), 2)

    def test_calculate_score_no_answer(self):
        # Test calculate_score() with no answer
        requirement = ListReq([], 2, "text", ["A", "B", "C"])
        self.assertEqual(requirement.calculate_score(None), 1)

    def test_calculate_score_answer_in_desired_answer(self):
        # Test calculate_score() with answer in desired answer list
        requirement = ListReq([], 2, "text", ["A", "B", "C"])
        self.assertEqual(requirement.calculate_score(["A", "D"]), 2)

    def test_calculate_score_answer_not_in_desired_answer(self):
        # Test calculate_score() with answer not in desired answer list
        requirement = ListReq([], 2, "text", ["A", "B", "C"])
        self.assertEqual(requirement.calculate_score(["D", "E"]), 0)

    def test_calculate_score_with_empty_desired_answer_list(self):
        req = ListReq(disqualifies=False, weight=1, text='test', desired_answer=[])
        score = req.calculate_score(['A', 'B'])
        self.assertIsNone(score)

    def test_calculate_score_with_single_desired_answer(self):
        req = ListReq(disqualifies=False, weight=1, text='test', desired_answer=['A'])
        score = req.calculate_score(['A', 'B'])
        self.assertEqual(score, 1)

    def test_calculate_score_with_non_list_answer(self):
        req = ListReq(disqualifies=False, weight=1, text='test', desired_answer=['A', 'B'])
        score = req.calculate_score('A')
        self.assertEqual(score, 1)

    def test_calculate_score_with_non_string_answer(self):
        req = ListReq(disqualifies=False, weight=1, text='test', desired_answer=['A', 'B'])
        score = req.calculate_score(['A', 1])
        self.assertEqual(score, 1)


if __name__ == '__main__':
    unittest.main()
