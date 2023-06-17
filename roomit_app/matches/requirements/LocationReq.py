import json
from .Requirement import Requirement
from shapely.geometry import Point, Polygon


class LocationReq(Requirement):
    def __init__(self, disqualifies, weight, text, desired_answer):
        super().__init__(disqualifies, weight, text)
        self._desired_answer = desired_answer

    # desired answer - polygon or rectangle
    def calculate_score(self, answer):

        # Parse the JSON string to get the area coordinates
        area_data = json.loads(self._desired_answer)
        point_data = json.loads(answer)

        # Create a list of shape objects (Markers, Rectangles, Polygons)
        coordinates_list = []
        for coordinate in area_data:
            coordinates_list.append((coordinate['lng'], coordinate['lat']))
        area = Polygon(coordinates_list)

        # Get the coordinate of the specific place
        specific_place_coordinate = (point_data['lng'], point_data['lat'])

        # Create a Point object from the specific place coordinate
        point = Point(specific_place_coordinate)

        # Check if the point is within thhe area
        is_within_area = area.contains(point)

        if is_within_area:
            return self._weight
        else:
            return 0

    def convert_answer_to_str(self, answer):
        return answer
