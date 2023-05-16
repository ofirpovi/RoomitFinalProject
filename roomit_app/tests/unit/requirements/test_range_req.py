import os
import django


os.environ['DJANGO_SETTINGS_MODULE'] = 'roomit_project.settings'
django.setup()

import unittest
from roomit_app.requirements.RangReq import RangeReq
from datetime import date, timedelta


class TestRangeReq(unittest.TestCase):
    def test_calculate_score_when_min_and_max_are_none(self):
        req = RangeReq([], 1, "Test", None, None)
        score = req.calculate_score(42)
        self.assertEqual(score, None)

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

        self.assertEqual(score, 0.5)

    def test_calculate_score_when_answer_is_not_an_int(self):
        req = RangeReq([], 1, "Test", 10, 20)

        with self.assertRaises(TypeError):
            req.calculate_score("not a number")

    def test_calculate_score_when_answer_is_within_range(self):
        req = RangeReq([], 1, "Test", 10, 20)

        score = req.calculate_score(15)

        self.assertEqual(score, 1)

    def test_calculate_score_when_answer_is_outside_range_and_outside_tolerance(self):
        req = RangeReq([], 1, "Test", 10, 20)

        score = req.calculate_score(35)

        self.assertEqual(score, 0)

    def test_both_min_max_none(self):
        requirement = RangeReq([], 10, "Test requirement", None, None)
        score = requirement.calculate_score(50)
        self.assertEqual(score, None)

    def test_answer_not_int(self):
        requirement = RangeReq([], 10, "Test requirement", 0, 100)
        with self.assertRaises(TypeError):
            requirement.calculate_score("not an int")
        with self.assertRaises(ValueError):
            requirement.calculate_score(-10)

    def test_answer_negative_number(self):
        requirement = RangeReq([], 10, "Test requirement", 0, 100)
        with self.assertRaises(ValueError):
            requirement.calculate_score(-10)

    def test_answer_outside_range(self):
        requirement = RangeReq([], 1, "Test requirement", 0, 100)
        score = requirement.calculate_score(200)
        self.assertEqual(score, 0)

    def test_answer_equal_to_min_max(self):
        requirement = RangeReq([], 10, "Test requirement", 0, 100)
        score = requirement.calculate_score(0)
        self.assertEqual(score, 10)

        score = requirement.calculate_score(100)
        self.assertEqual(score, 10)

    def setUp(self):
        self.range_req = RangeReq(False, 1, 'age', 18, 30)

    def test_answer_is_none(self):
        result = self.range_req.calculate_score(None)
        self.assertEqual(result, 0.5)

    def test_answer_is_not_a_number(self):
        with self.assertRaises(TypeError):
            self.range_req.calculate_score('not a number')

    def test_answer_is_negative(self):
        with self.assertRaises(ValueError):
            self.range_req.calculate_score(-1)

    def test_answer_is_greater_than_max(self):
        result = self.range_req.calculate_score(35)
        self.assertEqual(result, 0)

    def test_answer_is_less_than_min(self):
        result = self.range_req.calculate_score(17)
        self.assertEqual(result, 0)

    def test_answer_is_equal_to_min(self):
        result = self.range_req.calculate_score(18)
        self.assertEqual(result, 1)

    def test_answer_is_equal_to_max(self):
        result = self.range_req.calculate_score(30)
        self.assertEqual(result, 1)

    def test_answer_is_in_range(self):
        result = self.range_req.calculate_score(25)
        self.assertEqual(result, 1)

    def test_answer_birthdate_is_out_of_range(self):
        range_req = RangeReq(False, 1, 'birthdate', 18, 30)
        dob = date(1990, 1, 1)
        result = range_req.calculate_score(dob)
        self.assertEqual(result, 0)

    def test_answer_birthdate_is_on_range(self):
        range_req = RangeReq(False, 1, 'birthdate', 18, 33)
        dob = date(1990, 1, 1)
        result = range_req.calculate_score(dob)
        self.assertEqual(result, 1)
        dob = date(2005, 1, 1)
        result = range_req.calculate_score(dob)
        self.assertEqual(result, 1)

    def test_answer_birthdate_is_in_range(self):
        range_req = RangeReq(False, 1, 'birthdate', 18, 38)
        dob = date(1990, 1, 1)
        result = range_req.calculate_score(dob)
        self.assertEqual(result, 1)

    def test_answer_is_not_birthdate(self):
        range_req = RangeReq(False, 1, 'birthdate', 18, 30)
        with self.assertRaises(TypeError):
            range_req.calculate_score(25)

    def test_answer_birthday_is_in_future(self):
        # disqualifies = []
        # weight = 1
        # text = "birthdate"
        # min_age = 18
        # max_age = 30
        range_req = RangeReq([], 1, "birthdate", 18, 30)
        future_birthdate = date.today() + timedelta(days=365)
        with self.assertRaises(ValueError):
            range_req.calculate_score(future_birthdate)

    def test_non_datetime_birthdate(self):
        disqualifies = []
        weight = 1
        text = "birthdate"
        min_age = 18
        max_age = 30
        range_req = RangeReq(disqualifies, weight, text, min_age, max_age)
        non_datetime = "1990-01-01"
        with self.assertRaises(TypeError):
            range_req.calculate_score(non_datetime)

    def test_non_numeric_min_or_max(self):
        disqualifies = []
        weight = 1
        text = "age"
        min_age = "18"
        max_age = "30"
        range_req = RangeReq(disqualifies, weight, text, min_age, max_age)
        age = 25
        with self.assertRaises(TypeError):
            range_req.calculate_score(age)

    # todo: check where to check this case
    # def test_negative_min_or_max(self):
    #     disqualifies = []
    #     weight = 1
    #     text = "age"
    #     min_age = -18
    #     max_age = -10
    #     range_req = RangeReq(disqualifies, weight, text, min_age, max_age)
    #     age = 25
    #     with self.assertRaises(ValueError):
    #         range_req.calculate_score(age)

    def test_non_numeric_answer(self):
        disqualifies = []
        weight = 1
        text = "age"
        min_age = 18
        max_age = 30
        range_req = RangeReq(disqualifies, weight, text, min_age, max_age)
        answer = "twenty-five"
        with self.assertRaises(TypeError):
            range_req.calculate_score(answer)


if __name__ == '__main__':
    unittest.main()
