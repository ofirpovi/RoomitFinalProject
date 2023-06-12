import unittest
from roomit_app.matches.requirements import LocationReq


class LocationReqTest(unittest.TestCase):
    def setUp(self):
        # rectangle area coordinates
        self.rectangle_coordinates = '''
        [
            {"lat":31.16478137548193,"lng":34.4446716044355},
            {"lat":31.24841160751624,"lng":34.4446716044355},
            {"lat":31.24841160751624,"lng":34.57108747612921},
            {"lat":31.16478137548193,"lng":34.57108747612921}
        ]
        '''

        self.polygon_coordinates = '''
        [
            {"lat": 31.240985378021307, "lng": 34.56006028846006},
            {"lat": 31.32360964978387, "lng": 34.99472723125058},
            {"lat": 30.92484635000466, "lng": 35.069366863811624},
            {"lat": 30.554692710130748, "lng": 34.757636141094444},
            {"lat": 30.868282428573703, "lng": 34.366874943333784}
        ]
        '''

    def test_point_within_rectangle_area(self):
        specific_place_coordinate = '''{"lat": 31.211, "lng": 34.534}'''
        req = LocationReq([], 1, "Test", self.rectangle_coordinates)
        ans = req.calculate_score(specific_place_coordinate)
        self.assertEqual(ans, 1, "The point is within the area")

    def test_point_outside_rectangle_area(self):
        specific_place_coordinate = '''{"lat": 34.56789, "lng": 45.01234}'''
        req = LocationReq([], 1, "Test", self.rectangle_coordinates)
        ans = req.calculate_score(specific_place_coordinate)
        self.assertEqual(ans, 0, "The point is outside of the area")

    def test_point_within_polygon_area(self):
        specific_place_coordinate = '''{"lat": 31.268,"lng": 34.810}'''
        req = LocationReq([], 1, "Test", self.polygon_coordinates)
        ans = req.calculate_score(specific_place_coordinate)
        self.assertEqual(ans, 1, "The point is within the area")

    def test_point_outside_polygon_area(self):
        specific_place_coordinate = '''{"lat": 31.450,"lng": 34.650}'''
        req = LocationReq([], 1, "Test", self.polygon_coordinates)
        ans = req.calculate_score(specific_place_coordinate)
        self.assertEqual(ans, 0, "The point is outside of the area")

if __name__ == '__main__':
    unittest.main()
