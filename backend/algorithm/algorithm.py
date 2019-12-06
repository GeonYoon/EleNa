import heapq

class Path:
    
    def __init__(self,paths,threshold):
        self.min_distance = None
        self.min_distance_elevation = None
        self.paths = paths
        self.threshold = threshold

    # getter
    def get_min_distance(self):
        return self.min_distance
    
    # getter
    def get_min_elevation(self):
        return self.min_distance_elevation

    def add_elevation(self):
        pass

class Dijkstra:

    def __init__(self,paths):
        self.paths = paths
        pass
    

    def dijkstra(self):
        # error checking
        if not self.paths: return []
        
        q = []
        heapq.heappush(q,[])
        
