from django.test import TestCase
from .models import Model
import unittest
import heapq
import heapq
import collections

class Test_Algorithm:
    def __init__(self,model,threshold):
        self.model          = model
        self.threshold      = float(threshold)
        self.start_node     = self.model.start_node
        self.end_node       = self.model.end_node
    
    def get_shortest_path(self,src,dst):
        q       = []
        best    = {}
        heapq.heappush(q, (0,src))
        while q:
            # pop the element has the lowest cumulative distance in the queue
            cost,source = heapq.heappop(q)

            # stop if we reach to the destination
            if source == dst:
                break
        
            # check the neighbors
            for neighbor in self.model.get_neighbors(source):
                # update the distance 
                new_cost =  self.model.get_edge_length(source,neighbor) + cost
                # append the neighbor if it's a first time visit or visit here with a shortest distance
                if neighbor not in best or new_cost <  best[neighbor][0]:
                    heapq.heappush(q, (new_cost,neighbor))
                    best[neighbor] = [new_cost,source]
        return best

    def get_best_elevation(self,src,dst,total):
        q                 = []
        best              = {}
        initial_elevation = self.model.get_elevation(src)
        heapq.heappush(q, (initial_elevation,0,src))

        while q:
            # pop the element has the lowest elevation gain in the queue
            saved_elevation,cost,source = heapq.heappop(q)
            
            # stop if we reach to the destination
            if source == dst:
                break

            # check the neighbors
            for neighbor in self.model.get_neighbors(source):

                # find the elevation change from the current node to the next node
                elevation_difference = self.model.get_elevation(neighbor) - self.model.get_elevation(source)

                # if it's negative, change the difference to 0
                if elevation_difference < 0: elevation_difference = 0

                # add this to the total elevation
                saved_elevation += elevation_difference

                # update the distance 
                new_cost =  self.model.get_edge_length(source,neighbor) + cost

                # if the cumulative distance is over the threshold, ignore this path
                if new_cost > total * self.threshold: continue

                # append the neighbor if it's a first time visit or visit here with a shortest distance
                if neighbor not in best or new_cost <  best[neighbor][0]:
                    heapq.heappush(q, (saved_elevation,new_cost,neighbor))
                    best[neighbor] = [new_cost,source,saved_elevation]
        return best

class ModelTestCases(unittest.TestCase):

    def setUp(self):
        # Initializing a Model object
        start_coordinate = ["42.39718927454445", "-72.5226938724518"]
        end_coordinate = ["42.393399827433605", "-72.52405643463136"]
        self.model = Model(start_coordinate, end_coordinate)

    def test_get_edge_length(self):
        # Test edge length between neighboring node of start coordinate and one neighboring node of that node.
        actual_edge_length = int(self.model.get_edge_length(2264432148, 2264432160))
        expected_edge_length = 20
        self.assertEqual(actual_edge_length, expected_edge_length)

    def test_get_neighbors(self):
        # Test neighboring nodes of the neighboring node to the start coordinate.
        actual_neighbors = self.model.get_neighbors(2264432148).values
        expected_neighbor1 = 2264432160
        expected_neighbor2 = 2264432168
        expected_neighbor3 = 2264432133
        self.assertEqual(actual_neighbors[0], expected_neighbor1)
        self.assertEqual(actual_neighbors[1], expected_neighbor2)
        self.assertEqual(actual_neighbors[2], expected_neighbor3)

    def test_get_elevation(self):
        # Test elevation value of the neighboring node to the start coordinate.
        actual_elevation = self.model.get_elevation(2264432148)
        expected_elevation = 87.154
        self.assertEqual(actual_elevation, expected_elevation)

    def test_get_path_information_shortest_path(self):
        # Test the outputs of a shortest path without elevation.
        s_c = ["42.39718927454445", "-72.5226938724518"]
        e_c = ["42.396871486979514", "-72.52313375473024"]
        m = Model(s_c, e_c)
        path_map_shortest_path = Test_Algorithm(m, 2.0).get_shortest_path(2264432148, 2264432133)  
        actual_path, actual_total_distance, actual_total_elevation_gain = m.get_path_information(path_map_shortest_path)
        expected_path = [[42.3971725, -72.5227239], [42.3968766, -72.52315]]
        expected_total_distance = 48.118
        expected_total_elevation_gain = 0
        self.assertEqual(actual_path, expected_path)
        self.assertEqual(actual_total_distance, expected_total_distance)
        self.assertEqual(actual_total_elevation_gain, expected_total_elevation_gain)
    
    def test_get_path_information_best_elevation(self):
        # Test the outputs of a shortest path with elevation.
        s_c = ["42.39718927454445", "-72.5226938724518"]
        e_c = ["42.396871486979514", "-72.52313375473024"]
        m = Model(s_c, e_c)
        path_map_best_elevation = Test_Algorithm(m, 2.0).get_best_elevation(2264432148, 2264432133, 48.118)   
        actual_path, actual_total_distance, actual_total_elevation_gain = m.get_path_information(path_map_best_elevation)
        expected_path = [[42.3971725, -72.5227239], [42.3968766, -72.52315]]
        expected_total_distance = 48.118
        expected_total_elevation_gain = 0
        self.assertEqual(actual_path, expected_path)
        self.assertEqual(actual_total_distance, expected_total_distance)
        self.assertEqual(actual_total_elevation_gain, expected_total_elevation_gain)
        
if __name__ == '__main__':
    unittest.main()