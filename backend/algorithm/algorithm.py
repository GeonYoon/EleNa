import heapq
import heapq
import collections

class Navigator:
    
    def __init__(self,model,threshold):
        self.model          = model
        self.threshold      = float(threshold)
        self.start_node     = self.model.start_node
        self.end_node       = self.model.end_node
    
    def __get_shortest_path(self,src,dst):
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

    def __get_best_elevation(self,src,dst,total):
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
                elevation_difference = self.model.get_elevation(source) - self.model.get_elevation(neighbor)

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


    def get_the_path(self):

        # shortest path without considering elevation gain
        shortest_path_map = self.__get_shortest_path(self.start_node,self.end_node)
        coordinate_path,total_distance,total_elevation_gain  = self.model.get_path_information(shortest_path_map)

        # path with considering elevation gain
        elevation_path_map = self.__get_best_elevation(self.start_node,self.end_node,total_distance) # restrict with the total_distance from above
        coordinate_path2,total_distance2,total_elevation_gain2  = self.model.get_path_information(elevation_path_map)

        return coordinate_path2,total_distance2,total_elevation_gain2
        
