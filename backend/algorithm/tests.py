from django.test import TestCase
from .algorithm import Node, Graph, Path

class NodeTestCase(TestCase):
    def setUp(self):
        new_node = Node([1,2])
        self.latitude = latitude
        self.longitude = longitude

    def test_create_node(self):
        except_lat,expected_long = 1,2
        self.assertEqual(self.latitude,except_lat)
        self.assertEqual(self.longitude,expected_long)

# class GraphTestCase(TestCase):
#     def setUp(self):
        
#     def test_(self):

# class PathTestCase(TestCase):
#     def setUp(self):
#         pass
#     def test_(self):