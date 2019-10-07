import numpy as np
import time
import math
import sys
from itertools import cycle

'''
Reads in a tsp file, and converts the coordinate information into a dictionary of coordinate points
Input: file path (string)
Output: coordinate dictionary
'''
def read_tsp(file_name):
    coords = {}
    with open(file_name, "r") as file:
        data = file.readlines()
    
    for i in data:
        split_i = i.split(" ")
        if len(split_i) == 3:
            coords[split_i[0]] = (float(split_i[1]), float(split_i[2]))
    return coords

'''
Computes the Euclidean Distance between two coordinate points
Input: p1 (tuple), p2 (tuple)
Output: distance (float)
'''
def euc_dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

'''
Constructs and adjacency matrix for all points in the graph
Input: coordinates (dictionary)
Output: 2-D numpy array (float)
'''
def compute_distances(coords):
    dists = np.zeros((len(coords), len(coords)), np.float64)
    for i in range(0, len(dists)):
        for j in range(0, len(dists[i])):
            dists[i][j] = euc_dist( coords[str(i+1)], coords[str(j+1)])
    return dists

'''
Measures the length of a given tour
Input: path (list), adjacency matrix (numpy array)
Output: path length (float)
'''
def get_path_length(path, matrix):
    path_cycle = cycle(path)
    next_node = next(path_cycle)
    path_length = 0
    while True:
        this_node, next_node = next_node, next(path_cycle)
        if next_node == path[0]:
            break
        path_length = path_length + matrix[this_node, next_node]
    return path_length

'''
Solves the provided graph for the best tour
Input: coordinates (dictionary)
Output: None
'''
def greedy_tsp_solve(coords):
    d = compute_distances(coords)   #creates the adjacency matrix

    '''
    Helper function that finds the next node to be inserted into the tour
    Input: current path (list), adajency matrix (numpy array), list of unvisited nodes (list)
    Output: next node to insert,  the closest edge currently in the tour (tuple)
    '''
    def find_next(path, adj_matrix, node_list):
        closest_node = 0
        current_node = 0
        best_dist = math.inf
        for node in path[:-1]:  #checks each node except.  expects the list to have the starting node at the front and end to complete the cycle and ignores the second instance
            for i in node_list: #checks each unvisited node
                if adj_matrix[node][i] < best_dist:
                    closest_node = i
                    current_node = node
                    best_dist = adj_matrix[node][i]
        node_list.remove(closest_node)  #remove node from the unvisited node list
        return (closest_node, current_node)

    best_tour = None
    best_dist = math.inf
    order = []
    #For each starting node, find the best tour
    for i in range(0, len(d)):
        nodes = [i for i in range(0, len(d))]  #creat a list of unvisited nodes
        head = i
        in_order = [head]  #grab the insertion order
        path = [head, head] #initializes the path with the starting node
        nodes.remove(head)  
        while nodes:
            node, match = find_next(path, d, nodes) #get the next node to insert
            in_order.append(node)
            try:
                next_node = path[path.index(match) + 1] #check the neighbors of the closest edge currently in path to determine insertion order
                prev_node = path[path.index(match) - 1]
                if d[node][next_node] <= d[node][prev_node] or path.index(match) == 0:
                    path.insert(path.index(match)+1, node)
                else:
                    path.insert(path.index(match), node)
            except IndexError:  #catches edge case where the node must be inserted at the end of the path
                path.insert(len(path)-1, node)

        #compute tour length
        tour_length = get_path_length(path, d)
        if tour_length < best_dist:
            best_dist = tour_length
            best_tour = path
            order = in_order

    #increment nodes to match names rather than index (that is, set values to start at 1 rather than 0 to match .tsp file input)
    updated_best_tour = [i+1 for i in best_tour]
    updated_order = [i+1 for i in order]
    print("Best Tour: " + str(updated_best_tour))
    print("Best Tour Length: " + str(best_dist))
    print("Insertion Order: " + str(updated_order))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        coords = read_tsp(sys.argv[1])
        start_time = time.time()
        greedy_tsp_solve(coords)
        print("Run Time: " + str(time.time()-start_time) + " seconds")
    else:
        print("Incorrect input.  Please enter file path as second argument")
