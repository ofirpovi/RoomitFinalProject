import unittest
from ..requirements.YNReq import YNReq


class TestYNReq(unittest.TestCase):
    def setUp(self):
        self.req = YNReq(disqualifies=False, weight=1, text='Test', desired_answer='Y')

    def test_calculate_score_desired_answer_yes(self):
        self.assertEqual(self.req.calculate_score('Y'), 1)

    def test_calculate_score_desired_answer_no(self):
        self.assertEqual(self.req.calculate_score('N'), 0)

    def test_calculate_score_no_desired_answer(self):
        req = YNReq(disqualifies=False, weight=1, text='Test', desired_answer=None)
        self.assertEqual(req.calculate_score('Y'), 1)
        self.assertEqual(req.calculate_score('N'), 1)
        self.assertEqual(req.calculate_score(None), 1)

    def test_calculate_score_answer_yes_not_desired_answer(self):
        req = YNReq(disqualifies=False, weight=1, text='Test', desired_answer='N')
        self.assertEqual(req.calculate_score('Y'), 0)

    def test_calculate_score_answer_no_not_desired_answer(self):
        req = YNReq(disqualifies=False, weight=1, text='Test', desired_answer='Y')
        self.assertEqual(req.calculate_score('N'), 0)

    def test_calculate_score_answer_empty_string(self):
        self.assertEqual(self.req.calculate_score(''), 0)

    def test_calculate_score_answer_false(self):
        self.assertEqual(self.req.calculate_score(False), 0)

    def test_calculate_score_answer_zero(self):
        self.assertEqual(self.req.calculate_score(0), 0)

    def test_calculate_score_answer_one(self):
        self.assertEqual(self.req.calculate_score(1), 0)

    def test_calculate_score_answer_empty_list(self):
        self.assertEqual(self.req.calculate_score([]), 0)

    def test_calculate_score_answer_non_empty_list(self):
        self.assertEqual(self.req.calculate_score(['Y']), 0)


if __name__ == '__main__':
    unittest.main()
