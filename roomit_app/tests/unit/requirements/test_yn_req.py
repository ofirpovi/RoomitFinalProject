import unittest
from roomit_app.matches.requirements import YNReq


class TestYNReq(unittest.TestCase):
    def setUp(self):
        self.req = YNReq(disqualifies=False, weight=1, text='Test', desired_answer=True)

    def test_calculate_score_desired_answer_yes(self):
        self.assertEqual(self.req.calculate_score(True), 1)

    def test_calculate_score_desired_answer_no(self):
        self.assertEqual(self.req.calculate_score(False), 0)

    def test_calculate_score_no_desired_answer(self):
        req = YNReq(disqualifies=False, weight=1, text='Test', desired_answer=None)
        self.assertEqual(req.calculate_score(True), None)
        self.assertEqual(req.calculate_score(False), None)
        self.assertEqual(req.calculate_score(None), None)

    def test_calculate_score_answer_yes_not_desired_answer(self):
        req = YNReq(disqualifies=False, weight=1, text='Test', desired_answer=False)
        self.assertEqual(req.calculate_score(True), 0)

    def test_calculate_score_answer_no_not_desired_answer(self):
        with self.assertRaises(TypeError):
            self.req.calculate_score('N')

    def test_calculate_score_answer_empty_string(self):
        with self.assertRaises(TypeError):
            self.req.calculate_score('')

    def test_calculate_score_answer_false(self):
        self.assertEqual(self.req.calculate_score(False), 0)

    def test_calculate_score_answer_one(self):
        with self.assertRaises(TypeError):
            self.req.calculate_score(1)

    def test_calculate_score_answer_empty_list(self):
        with self.assertRaises(TypeError):
            self.req.calculate_score([])

    def test_calculate_score_answer_non_empty_list(self):
        with self.assertRaises(TypeError):
            self.req.calculate_score(['Y'])

    def test_calculate_score_with_desired_answer(self):
        yn_req = YNReq("disqualifies", 5, "Are you a student?", True)
        self.assertEqual(yn_req.calculate_score(True), 5)
        self.assertEqual(yn_req.calculate_score(False), 0)

    def test_calculate_score_without_desired_answer(self):
        yn_req = YNReq("disqualifies", 5, "Are you a student?", None)
        self.assertIsNone(yn_req.calculate_score(True))

    def test_calculate_score_with_non_bool_answer(self):
        yn_req = YNReq("disqualifies", 5, "Are you a student?", True)
        with self.assertRaises(TypeError):
            yn_req.calculate_score(1)
        with self.assertRaises(TypeError):
            yn_req.calculate_score("yes")
        with self.assertRaises(TypeError):
            yn_req.calculate_score(0.5)

    # todo: check where to raise this
    # def test_desired_answer_not_bool(self):
    #     with self.assertRaises(TypeError):
    #         req = YNReq(False, 1, "Is this a boolean answer?", "Yes")

    def test_desired_answer_none(self):
        req = YNReq(False, 1, "Is this a boolean answer?", None)
        self.assertIsNone(req.calculate_score(True))

    def test_matching_bool_answer(self):
        req = YNReq(False, 2, "Is this a boolean answer?", True)
        self.assertEqual(req.calculate_score(True), 2)

    def test_non_matching_bool_answer(self):
        req = YNReq(False, 2, "Is this a boolean answer?", False)
        self.assertEqual(req.calculate_score(True), 0)

    def test_answer_not_bool(self):
        with self.assertRaises(TypeError):
            req = YNReq(False, 1, "Is this a boolean answer?", True)
            req.calculate_score("Yes")

if __name__ == '__main__':
    unittest.main()
