
import math
import Requirement
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
        if self._distance:
            answer = self.calculate_distance(answer, self._address)
        if self._max is None:
            if self._min > answer:
                return 0
            else:
                return self._weight
        if answer < 0:
            raise ValueError("Answer could not be a negative value")
        if type(answer) is not int:
            raise TypeError("Answer should be a number")

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
        if self._distance:
            answer = self.calculate_distance(answer, self._address)
        return answer

    def calculate_distance(self, address1, address2):
        # create a geolocator object
        geolocator = Nominatim(user_agent="geoapiExercises")

        # convert the addresses to coordinates
        location1 = geolocator.geocode(address1)
        location2 = geolocator.geocode(address2)

        # calculate the distance between the coordinates
        distance = geodesic((location1.latitude, location1.longitude),
                            (location2.latitude, location2.longitude)).kilometers

        return int(distance)
