import numpy as np
import math

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

def BFS(matrix):
    head = 0
    queue = [[head]]
    best_dist = math.inf

    while queue:
        path = queue.pop(0)
        node = path[-1]   
        if 10 in path:
            dist = sum(path)
            if dist < best_dist:
                best_dist = dist
        print("Path: " + str(path))
        print("Checking node: " + str(node))
        for j in range(0,len(matrix[node])):
            if matrix[node][j] > 0:
                new_path = path.copy()
                new_path.append(j)
                queue.append(new_path)
                print("Visiting " + str(j+1))
    print(best_dist)

def DFS(matrix):
    return True

BFS(adj_matrix)