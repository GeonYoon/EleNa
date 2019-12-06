from django.db import models
from django.conf import settings
import networkx as nx
import osmnx as ox
from geopy.geocoders import Nominatim
import os
file_path = os.path.join(settings.BASE_DIR, 'G_drive.graphml')

# Create your models here.
class Model:
    import osmnx as ox
    import networkx as nx

    def __init__(self,start,end):
        self.ox.config(use_cache=True, log_console=True)
        self.ox.__version__
        self.G_drive            = ox.load_graphml(file_path)
        self.nodes, self.edges  = ox.graph_to_gdfs(self.G_drive)
        self.start_node         = self.__get_nearest_node(float(start[0]),float(start[1]))
        self.end_node           = self.__get_nearest_node(float(end[0]),float(end[1]))
    
    def __get_nearest_node(self,latitude, longitude):
        node = ox.get_nearest_node(self.G_drive, (latitude, longitude))
        return node

    def __get_total_elevation_gain(self,path):
        if len(path) <= 1: return 0
        total,prev = 0,path[0]
        for node in path[1:]:
            elevation_difference = self.get_elevation(prev) - self.get_elevation(node)
            if elevation_difference > 0:
                total += elevation_difference
        return total

    def __get_coordinate(self,node):
        latitude    =  self.G_drive.nodes[node]['y']
        longitude   =  self.G_drive.nodes[node]['x']
        return [latitude,longitude]

    def get_edge_length(self,startNode, endNode):
        return self.G_drive.edges[startNode, endNode, 0]['length']

    def get_neighbors(self,node):
        filtered = self.edges[self.edges.u == node]
        return filtered['v']

    def get_elevation(self,node):
        return float(self.G_drive.nodes[node]['elevation'])

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
            coordinate_path.append(self.__get_coordinate(end_node))

            # update it
            end_node              = prev_node

            # if the updated node is a start node, append it
            if end_node == self.start_node:
                node_path.append(self.start_node)
                coordinate_path.append(self.__get_coordinate(self.start_node))
        
        node_path.reverse()
        coordinate_path.reverse()
        total_elevation_gain = self.__get_total_elevation_gain(node_path)
        return coordinate_path,total_distance,total_elevation_gain