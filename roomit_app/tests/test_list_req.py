import unittest
from ..requirements.ListReq import ListReq


class ListReqTest(unittest.TestCase):

    def test_calculate_score_desired_answer_none(self):
        req = ListReq(disqualifies=False, weight=1, text="test", desired_answer=None)
        self.assertEqual(req.calculate_score([]), 1)

    def test_calculate_score_answer_none(self):
        req = ListReq(disqualifies=False, weight=1, text="test", desired_answer=['A'])
        self.assertEqual(req.calculate_score(None), 0)

    def test_calculate_score_desired_answer_is_disjoint(self):
        req = ListReq(disqualifies=False, weight=1, text="test", desired_answer=['A'])
        self.assertEqual(req.calculate_score(['B']), 0)

    def test_calculate_score_answer_is_disjoint(self):
        req = ListReq(disqualifies=False, weight=1, text="test", desired_answer=['A'])
        self.assertEqual(req.calculate_score(['B']), 0)

    def test_calculate_score_answer_is_subset(self):
        req = ListReq(disqualifies=False, weight=1, text="test", desired_answer=['A'])
        self.assertEqual(req.calculate_score(['A', 'B']), 1)

    def test_calculate_score_answer_is_superset(self):
        req = ListReq(disqualifies=False, weight=1, text="test", desired_answer=['A', 'B'])
        self.assertEqual(req.calculate_score(['A']), 1)

    def test_calculate_score_desired_answer_is_empty(self):
        requirement = ListReq(False, 5, "test", set())
        score = requirement.calculate_score(None)
        self.assertEqual(score, 0)

    def test_calculate_score_answer_is_none(self):
        requirement = ListReq(False, 5, "test", {"A", "B", "C"})
        score = requirement.calculate_score(None)
        self.assertEqual(score, 0)

    def test_calculate_score_answer_does_not_intersect_desired_answer(self):
        requirement = ListReq(False, 5, "test", {"A", "B", "C"})
        score = requirement.calculate_score({"D", "E", "F"})
        self.assertEqual(score, 0)

    def test_calculate_score_answer_intersects_desired_answer(self):
        requirement = ListReq(False, 5, "test", {"A", "B", "C"})
        score = requirement.calculate_score({"C", "D", "E"})
        self.assertEqual(score, 5)

if __name__ == '__main__':
    unittest.main()
