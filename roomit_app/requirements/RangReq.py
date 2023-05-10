import math
from .Requirement import Requirement
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
from datetime import date

class RangeReq(Requirement):
    def __init__(self, disqualifies, weight, text, min, max, distance=False, address=None):
        super().__init__(disqualifies, weight, text)
        self._min = min
        self._max = max
        self._distance = distance
        self._address = address

    def calculate_score(self, answer):
        # if age requirement calculate age from birthdate
        if self._text == "birthdate":
            answer = self.calculate_age(answer)
        # if there is a desired answer for the requirement but there is no answer
        if answer is None:
            return self._weight / 2
        # check that answer is a number
        elif type(answer) is not int and type(answer) is not float:
            raise TypeError("Answer should be a number, got -- ", answer, " of type -- ", type(answer))
        # check that answer is a non-negative number
        elif answer < 0:
            raise ValueError("Answer should be a non-negative number")
        # if there is no desired answer
        if self._max is None and self._min is None:
            return None
        # if there is no desired max
        elif self._max is None:
            # if answer is equal to or greater than the desired min
            if self._min <= answer:
                return self._weight
            # if answer is less than desired min
            else:
                return 0
        # if there is no desired min
        elif self._min is None:
            # if answer is equal to or less than desired max
            if self._max >= answer:
                return self._weight
            # if answer is greater than desired max
            else:
                return 0
        # if answer is in desired range
        elif answer in range(self._min, self._max + 1):
            return self._weight
        # if there is a desired range but answer is not in range
        else:
            return 0

    def calculate_age(self, dob):
        today = date.today()
        # check that birthday is of type date
        if type(dob) is not date:
            raise TypeError("Birthday must be a date")
        # check that the birthdate has past
        if dob > today:
            raise ValueError("Birthday must be a date from the past")
        # calculate age from given birthdate
        age = today.year - dob.year - ((today.month, today.day) <
             (dob.month, dob.day))
        return age

    def convert_answer_to_str(self, answer):
        return answer
