# install dependencies 
import networkx as nx
import osmnx as ox
import requests
from geopy.geocoders import Nominatim

# initial set up 
ox.config(use_cache=True, log_console=True)
ox.__version__
G_drive = ox.load_graphml('G_drive.graphml')
nodes, edges = ox.graph_to_gdfs(G_drive)

def get_nearest_node(G, latitude, longitude):
    node = ox.get_nearest_node(G, (latitude, longitude))
    return node

def get_edge_length(G, startNode, endNode):
    return G.edges[startNode, endNode, 0]['length']

def get_neighbors(edges_list,node):
    filtered = edges_list[edges_list.u == node]
    return filtered['v']

def get_elevation(G,node):
    return float(G.nodes[node]['elevation'])

start = ox.geocode("585 E Pleasant St, Amherst, MA 01002")
end = ox.geocode("175 University Dr, Amherst, MA 01002")
nearest_start = get_nearest_node(G_drive, start[0], start[1])
nearest_end = get_nearest_node(G_drive, end[0], end[1])

# print("start: ",nearest_start)
# print("end: ",nearest_end)
# print("-----------------------")

# start_elevation = get_elevation(G_drive,nearest_start)
# neighbors = get_neighbors(edges,nearest_start)
# for neighbor in neighbors:
#     print("node: ",neighbor)
#     print("length: ",get_edge_length(G_drive,nearest_start,neighbor))
#     print("elevation change: ",get_elevation(G_drive,neighbor) - start_elevation) 
#     print("-----------------------")


import heapq
import collections

def elevation_cal(path):
    total = 0
    prev = path[0]
    for node in path[1:]:
        elevation_difference = get_elevation(G_drive,prev) - get_elevation(G_drive,node)
        if elevation_difference > 0:
            total += elevation_difference
    return total
        

def get_shortest_path(src,dst):
    rt = []
    q = []
    best = {}
    heapq.heappush(q, (0,src))
    while q: # fix in the future
        
        cost,source = heapq.heappop(q)
        if source == dst:
            break
                
        for neighbor in get_neighbors(edges,source):
            new_cost =  get_edge_length(G_drive,source,neighbor) + cost
            if neighbor not in best or new_cost <  best[neighbor][0]:
                heapq.heappush(q, (new_cost,neighbor))
                best[neighbor] = [new_cost,source]
    return best

def elevation_cal(path):
    total = 0
    prev = path[0]
    for node in path[1:]:
        elevation_difference = get_elevation(G_drive,prev) - get_elevation(G_drive,node)
        if elevation_difference > 0:
            total += elevation_difference
    return total
        

def get_shortest_path(src,dst):
    rt = []
    q = []
    best = {}
    heapq.heappush(q, (0,src))
    while q: # fix in the future
        
        cost,source = heapq.heappop(q)
        if source == dst:
            break
                
        for neighbor in get_neighbors(edges,source):
            new_cost =  get_edge_length(G_drive,source,neighbor) + cost
            if neighbor not in best or new_cost <  best[neighbor][0]:
                heapq.heappush(q, (new_cost,neighbor))
                best[neighbor] = [new_cost,source]
    return best

def get_best_elevation2(src,dst,total):
    rt = []
    q = []
    best = {}
    heapq.heappush(q, (0,src))
    while q: # fix in the future

        # pop the element has the lowest elevation gain in the queue
        cost,source = heapq.heappop(q)
        # stop if we reach to the destination
        if source == dst:
            break

        # check the neighbors
        for neighbor in get_neighbors(edges,source):

            # find the elevation change from the current node to the next node
            elevation_difference = get_elevation(G_drive,source) - get_elevation(G_drive,neighbor)

            # if it's negative, change the difference to 0
            if elevation_difference < 0: elevation_difference = 0

            # update the distance 
            new_cost =  get_edge_length(G_drive,source,neighbor) + cost + elevation_difference*100

            if neighbor not in best or new_cost <  best[neighbor][0]:
                heapq.heappush(q, (new_cost,neighbor))
                best[neighbor] = [new_cost,source]

    return best

def get_best_elevation3(src,dst,total):
    rt = []
    q = []
    best = {}
    initial_elevation = get_elevation(G_drive,src)
    heapq.heappush(q, (initial_elevation,0,src))
    while q: # fix in the future

        # pop the element has the lowest elevation gain in the queue
        saved_elevation,cost,source = heapq.heappop(q)
        # stop if we reach to the destination
        if source == dst:
            break

        # check the neighbors
        for neighbor in get_neighbors(edges,source):

            # find the elevation change from the current node to the next node
            elevation_difference = get_elevation(G_drive,source) - get_elevation(G_drive,neighbor)

            # if it's negative, change the difference to 0
            if elevation_difference < 0: elevation_difference = 0

            # add this to the total elevation
            saved_elevation += elevation_difference

            # update the distance 
            new_cost =  get_edge_length(G_drive,source,neighbor) + cost

            if neighbor not in best or new_cost <  best[neighbor][0]:
                heapq.heappush(q, (saved_elevation,new_cost,neighbor))
                best[neighbor] = [new_cost,source,new_cost]

    return best


def get_best_elevation(src,dst,total):
    rt = []
    q = []
    best = {}
    initial_elevation = get_elevation(G_drive,src)
    heapq.heappush(q, (initial_elevation,0,src))
    while q: # fix in the future

        # pop the element has the lowest elevation gain in the queue
        saved_elevation,cost,source = heapq.heappop(q)
        # stop if we reach to the destination
        if source == dst:
            break

        # check the neighbors
        for neighbor in get_neighbors(edges,source):
            # update the distance 

            new_cost =  get_edge_length(G_drive,source,neighbor) + cost

            # find the elevation change from the current node to the next node
            elevation_difference = get_elevation(G_drive,source) - get_elevation(G_drive,neighbor)

            # if it's negative, change the difference to 0
            if elevation_difference < 0: elevation_difference = 0

            # add this to the total elevation
            saved_elevation += elevation_difference

            # if the total travel distance is over shortest_distance * 1.5(for now), don't do anything and move to the next loop
            if new_cost > total*1.5: continue

            # if I have never visited this or I have nec
            if neighbor not in best or saved_elevation <  best[neighbor][0]:
                heapq.heappush(q, (saved_elevation,new_cost,neighbor))
                best[neighbor] = [saved_elevation,source]
    return best

print("------------------------")
print("answer:")
pat = nx.shortest_path(G_drive,nearest_start,nearest_end)
length = nx.shortest_path_length(G=G_drive, source=nearest_start, target=nearest_end, weight='length')

print(pat)
print("distance:", length)
print("elevation gain", elevation_cal(pat))

print("------------------------")
print("my answer:")
best = get_shortest_path(nearest_start,nearest_end)
path = []
total = 0
travel = nearest_end
while travel != nearest_start:
    path.append(travel)
    prev = best[travel][1]
    total += get_edge_length(G_drive,prev,travel)
    travel = prev

path.append(nearest_start)
path.reverse()
print(path)
print("distance:", total)
print("elevation gain", elevation_cal(path))


print("------------------------")
print("my answer for elevation:")
best2 = get_best_elevation3(nearest_start,nearest_end,total)
path2 = []
total2 = 0
travel = nearest_end
while travel != nearest_start:
    path2.append(travel)
    prev = best2[travel][1]
    total2 += get_edge_length(G_drive,prev,travel)
    travel = prev

path2.append(nearest_start)
path2.reverse()
print(path2)
print("distance:", total2)
print("elevation gain", elevation_cal(path2))




