from django.test import TestCase
from .models import Model
import unittest


class ModelTestCases(unittest.TestCase):

    def setUp(self):
        start_coordinate = ["42.39718927454445", "-72.5226938724518"] # Sylvan Brown Hall
        end_coordinate = ["42.393399827433605", "-72.52405643463136"] # Worcester Dining
        self.model = Model(start_coordinate, end_coordinate)
    
    def test_get_edge_length(self):
        actual_edge_length = int(self.model.get_edge_length(66732034, 1843788747))
        expected_edge_length = 327
        self.assertEqual(actual_edge_length, expected_edge_length)

    def test_get_neighbors(self):
        actual_neighbors = self.model.get_neighbors(66732034).values
        expected_neighbor1 = 1843788747
        expected_neighbor2 = 1669520735
        expected_neighbor3 = 66714254
        self.assertEqual(actual_neighbors[0], expected_neighbor1)
        self.assertEqual(actual_neighbors[1], expected_neighbor2)
        self.assertEqual(actual_neighbors[2], expected_neighbor3)

    def test_get_elevation(self):
        actual_elevation = self.model.get_elevation(6630490116)
        expected_elevation = 75.833
        self.assertEqual(actual_elevation, expected_elevation)

    # def test_get_path_information(self):
        # pathmap = {1843788747: [1, 66732034]}
        # actual_path, actual_total_distance, actual_total_elevation_gain = self.model.get_path_information(pathmap)

                
if __name__ == '__main__':
    unittest.main()