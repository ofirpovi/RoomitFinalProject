import math
from .Requirement import Requirement
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic


class RangeReq(Requirement):
    def __init__(self, disqualifies, weight, text, min, max, distance=False, address=None):
        super().__init__(disqualifies, weight, text)
        self._min = min
        self._max = max
        self._distance = distance
        self._address = address

    def calculate_score(self, answer):
        if type(answer) is not int:
            raise TypeError("Answer should be a number")
        if answer <= 0:
            raise ValueError("Answer should be a non-negative number")
        if self._max is None and self._min is None:
            return self._weight
        if self._max is None or answer is None:
            if answer is None or self._min > answer:
                return 0
            else:
                return self._weight


        if answer in range(self._min, self._max):
            return self._weight
        else:
            mean = (self._max + self._min) / 2
            stde = (self._max - self._min) / 2
            deviation = abs(answer-mean)
            ans_stde = math.floor(deviation/stde)

            if ans_stde > 3:
                return 0
            else:
                return (1-0.05*ans_stde)*self._weight

    def convert_answer_to_str(self, answer):
        return answer
