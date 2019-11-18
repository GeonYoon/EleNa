class Node:
    
    def __init__(self,data):
        self.latitude   = data[0]
        self.longitude  = data[1]
        self.elevation  = None
        self.neighbors = []

    def add_elevation(self,elevation):
        self.elevation = elevation

class Graph:
    
    def __init__(self):
        self.start_point = None
        self.end_point = None
        self.graph = None

    def make_graph(lst):
        pass
    
class Path:
    
    def __init__(paths):
        self.min_distance = None

    def min_path(self,Node[]): 
        
        # run Dijkstra without considering elevation
        # run Dijkstra targetting elevation + restrict the alogrithm with the min distacne
        pass

    def dijkstra(nodes):
        pass

