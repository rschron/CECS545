import numpy as np
import math
from itertools import cycle
import time

#Define the adjacency matrix representing the input graph
adj_matrix = np.array(
    [[0, 21.04751232,  8.20985338, 25.95058426, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 18.99134667, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 24.8329539, 13.32804842, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 17.25084287, 12.29902174, 13.1261299, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 15.8304564, 31.91182923, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8.69158453, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 8.30976298, 24.69534985, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 13.636152, 10.58180794, 16.20664777],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12.28904358],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12.88564307],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    np.float64
)

'''
Helper function that takes a given path and computes the path length.  This
is used to test candidate paths.
Input: path (list), matrix (2d array)
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
Breadth-First Search solution to the shortest path problem.
Input: matrix (2d array)
Output: None
'''
def BFS(matrix):
    start_time = time.time()
    head = 0
    queue = [[head]]
    best_dist = math.inf
    best_path = []
    trans_count = 0

    while queue:
        path = queue.pop(0)
        node = path[-1]  
        if 10 in path:
            dist = get_path_length(path, matrix)
            if dist < best_dist:
                best_dist = dist
                best_path = path.copy()
        for j in range(0,len(matrix[node])):
            if matrix[node][j] > 0:
                #trans_count = trans_count + 1
                new_path = path.copy()
                new_path.append(j)
                queue.append(new_path)
    print("BFS Best Path: " +str(best_path))
    print("BFS Best Distance: " + str(best_dist))
    print("BFS Time: " + str(time.time()-start_time))
    #print("BFS Transitions: " + str(trans_count))
    print()

'''
Depth-First Search solution to the shortest path problem
Input: matrix (2d array)
Output: None
'''
def DFS(matrix):
    start_time = time.time()
    path_collection = []
    '''
    Recursive function that looks for potential paths
    Input: matrix (2d array), path (list)
    Output: None
    '''
    def DFS_recurse(matrix, path):
        node = path[-1]

        for i in range(0, len(matrix[node])):
            if matrix[node][i] > 0:
                new_path = path.copy()
                new_path.append(i)
                DFS_recurse(matrix, new_path)
        path_collection.append(path)
    
    head = [0]
    best_path = []
    best_dist = math.inf
    
    DFS_recurse(matrix, head)
    for i in path_collection:
        if 10 in i:
            d = get_path_length(i, matrix)
            if  d < best_dist:
                best_dist = d
                best_path = i

    print("DFS Best Path: " + str(best_path))
    print("DFS Best Dist: " + str(best_dist))
    print("DFS Time: " + str(time.time()-start_time))
    #print("DFS Transitions: " + str(len(path_collection) - 1))
    print()

#Run the DFS implementation
DFS(adj_matrix)

#Run the BFS implementation
BFS(adj_matrix)