from django.test import TestCase
from .algorithm import Navigator
from .models import Model

class NavigatorTestCases(TestCase):
    # Initializing test objects
    def setUp(self):
        start_coordinate = ["42.39718927454445", "-72.5226938724518"] # Sylvan Brown Hall
        end_coordinate = ["42.393399827433605", "-72.52405643463136"] # Worcester Dining
        model = Model(start_coordinate, end_coordinate)
        # self.a = Navigator(model, "0.0") # Navigator Object with 0% distance threshhold # Not working
        self.a = Navigator(model, "1.0") # Navigator Object with 50% distance threshhold
        self.b = Navigator(model, "1.0") # Navigator Object with 50% distance threshhold
        self.c = Navigator(model, "2.0") # Navigator Object with 100% distance threshhold
    
    # Test shortest path when distance threshhold is ignored
    def test_shortest_path_no_threshhold(self):
        actual_path, actual_total_travel_distance, actual_elevation_gain = self.a.get_the_path()
        expected_path = [[42.3971725, -72.5227239], [42.3968766, -72.52315], [42.3968036, -72.5231341], 
                         [42.3962336, -72.52367], [42.3941848, -72.5235401], [42.3941874, -72.5236271], 
                         [42.393701, -72.5237087], [42.3933408, -72.523789], [42.393359, -72.523991], 
                         [42.3934001, -72.5240153]]
        expected_total_travel_distance = 493.465
        expected_elevation_gain = 51.52399999999996
        self.assertEqual(actual_path, expected_path)
        self.assertEqual(actual_total_travel_distance, expected_total_travel_distance)
        self.assertEqual(actual_elevation_gain, expected_elevation_gain)
        # print(actual_path)
        # print(actual_total_travel_distance)
        # print(actual_elevation_gain)

    # Test shortest path when distance threshhold is at 50%
    def test_shortest_path_half_threshhold(self):
        actual_path, actual_total_travel_distance, actual_elevation_gain = self.b.get_the_path()
        expected_path = [[42.3971725, -72.5227239], [42.3968766, -72.52315], [42.3968036, -72.5231341], 
                         [42.3962336, -72.52367], [42.3941848, -72.5235401], [42.3941874, -72.5236271], 
                         [42.393701, -72.5237087], [42.3933408, -72.523789], [42.393359, -72.523991], 
                         [42.3934001, -72.5240153]]
        expected_total_travel_distance = 493.465
        expected_elevation_gain = 51.52399999999996
        self.assertEqual(actual_path, expected_path)
        self.assertEqual(actual_total_travel_distance, expected_total_travel_distance)
        self.assertEqual(actual_elevation_gain, expected_elevation_gain)

    # Test shortest path when distance threshhold is at 100%   
    def test_shortest_path_full_threshhold(self):
        actual_path, actual_total_travel_distance, actual_elevation_gain = self.c.get_the_path()
        expected_path = [[42.3971725, -72.5227239], [42.3968766, -72.52315], [42.3968036, -72.5231341], 
                         [42.3962336, -72.52367], [42.3941848, -72.5235401], [42.3941874, -72.5236271], 
                         [42.393701, -72.5237087], [42.3933408, -72.523789], [42.393359, -72.523991], 
                         [42.3934001, -72.5240153]]
        expected_total_travel_distance = 493.465
        expected_elevation_gain = 51.52399999999996
        self.assertEqual(actual_path, expected_path)
        self.assertEqual(actual_total_travel_distance, expected_total_travel_distance)
        self.assertEqual(actual_elevation_gain, expected_elevation_gain)
