class Node:
    def __init__(self,data):
        self.latitude   = data[0]
        self.longitude  = data[1]
        self.elevation  = None
        self.neighbors = []

    def add_elevation(self,elevation):
        self.elevation = elevation  
class Graph:    
    def __init__(self,paths):
        self.start_point = None
        self.end_point = None
        self.graph = None

    def make_graph(self,lst):
        return 
    
class Path:
    
    def __init__(self,graph):
        self.min_distance = None
        self.min_distance_elevation = None
        self.graph = graph

    # run Dijkstra without considering elevation
    def min_path_distance(self): 
        return 

    # run Dijkstra targetting elevation + restrict the alogrithm with the min distacne
    def min_path_elevation(self):
        return
