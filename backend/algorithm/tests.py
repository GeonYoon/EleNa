from django.test import TestCase
from algorithm import Navigator
import unittest


class Node:
    def __init__(self,val,elevation):
        self.val        = val
        self.neighbor   = []
        self.elevation  = elevation

class Test_Model:

    def __init__(self):
        
        # access to the distance 
        self.distance = {}

        # create nodes
        A = Node('a',0)
        B = Node('b',2)
        C = Node('c',1)
        D = Node('d',0)

        # dummy coordinate
        self.start_coordinate = 'a'
        self.end_coordinate = 'd'

        # build the relationships
        self.distance[A,C] = 1
        self.distance[A,B] = 2
        self.distance[C,D] = 6
        self.distance[B,D] = 3 

        # define neighbors
        A.neighbor.append(C)
        A.neighbor.append(B)
        C.neighbor.append(D)
        B.neighbor.append(D)

        # define src and dest
        self.start_node     = A
        self.end_node       = D 

    def __get_total_elevation_gain(self,path):
        if len(path) <= 1: return 0
        total,prev = 0,path[0]
        for node in path[1:]:
            elevation_difference = self.get_elevation(node) - self.get_elevation(prev)
            if elevation_difference > 0:
                total += elevation_difference
        return total
    
    def get_edge_length(self,startNode, endNode):
        return self.distance[startNode,endNode]
    
    def get_neighbors(self,node):
        return node.neighbor

    def get_elevation(self,node):
        return node.elevation
    
    def get_path_information(self,path_map):
        node_path               = []    #[lang,long,distance,elevation]
        coordinate_path         = []
        total_distance          = 0
        total_elevation_gain    = 0
        end_node                = self.end_node  

        while end_node != self.start_node:
            # append the node
            node_path.append(end_node)

            prev_node             = path_map[end_node][1]
            dinstance_travel      = self.get_edge_length(prev_node,end_node)
            total_distance       += dinstance_travel
            coordinate_path.append(end_node.val)

            # update it
            end_node              = prev_node

            # if the updated node is a start node, append it
            if end_node == self.start_node:
                node_path.append(self.start_node)
                coordinate_path.append(end_node.val)
        
        node_path.reverse()
        coordinate_path.reverse()
        total_elevation_gain = self.__get_total_elevation_gain(node_path)
        return coordinate_path,total_distance,total_elevation_gain

class NavigatorTestCase(unittest.TestCase): 

    def setUp(self): 
        self.my_model            = Test_Model()
        # my_navigator        = Navigator(my_model,1)
    
    def test_shortest_path_no_threshold(self):
        my_navigator        = Navigator(self.my_model ,2.0)
        shortest_pack,elevation_pack = my_navigator.get_the_path()

        path                    = shortest_pack[0]
        total_distance          = shortest_pack[1]
        total_elevation         = shortest_pack[2]

        expected_path           = ['a','b','d']
        expected_total_distance = 5
        expected_elevation_gain = 2

        self.assertEqual(path,expected_path)
        self.assertEqual(total_distance,expected_total_distance)
        self.assertEqual(total_elevation,expected_elevation_gain)
        
    
    def test_best_elevation_no_threshold(self):
        my_navigator        = Navigator(self.my_model ,2.0)
        shortest_pack,elevation_pack = my_navigator.get_the_path()

        path                    = elevation_pack[0]
        total_distance          = elevation_pack[1]
        total_elevation         = elevation_pack[2]

        expected_path           = ['a','c','d']
        expected_total_distance = 7
        expected_elevation_gain = 1

        self.assertEqual(path,expected_path)
        self.assertEqual(total_distance,expected_total_distance)
        self.assertEqual(total_elevation,expected_elevation_gain)
        
    def test_shortest_path_yes_threshold(self):
        my_navigator        = Navigator(self.my_model ,2.0)
        shortest_pack,elevation_pack = my_navigator.get_the_path()

        path                    = shortest_pack[0]
        total_distance          = shortest_pack[1]
        total_elevation         = shortest_pack[2]

        expected_path           = ['a','b','d']
        expected_total_distance = 5
        expected_elevation_gain = 2

        self.assertEqual(path,expected_path)
        self.assertEqual(total_distance,expected_total_distance)
        self.assertEqual(total_elevation,expected_elevation_gain)
        

    def test_best_elevation_yes_threshold(self):
        my_navigator        = Navigator(self.my_model ,2.0)
        shortest_pack,elevation_pack = my_navigator.get_the_path()

        path                    = shortest_pack[0]
        total_distance          = shortest_pack[1]
        total_elevation         = shortest_pack[2]

        expected_path           = ['a','b','d']
        expected_total_distance = 5
        expected_elevation_gain = 2

        self.assertEqual(path,expected_path)
        self.assertEqual(total_distance,expected_total_distance)
        self.assertEqual(total_elevation,expected_elevation_gain)
        
        
if __name__ == '__main__':
    unittest.main()