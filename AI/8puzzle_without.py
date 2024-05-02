import copy  # Importing the copy module for deep copying lists
from heapq import heappush, heappop  # Importing heappush and heappop functions from heapq module

n = 3  # Size of the puzzle (3x3)

# Directions for moving the empty tile (up, left, down, right)
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

# Priority Queue class for managing nodes based on their costs
class priorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, k):
        heappush(self.heap, k)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        return not self.heap

# Node class representing a state in the puzzle
class node:
    def __init__(self, parent, mat, empty_tile_pos, cost, level):
        self.parent = parent  # Parent node
        self.mat = mat  # Configuration of the puzzle
        self.empty_tile_pos = empty_tile_pos  # Position of the empty tile
        self.cost = cost  # Total cost of the node
        self.level = level  # Level of the node in the search tree

    def __lt__(self, nxt):
        return self.cost < nxt.cost  # Comparison method for nodes based on cost

# Function to calculate the total cost of a state in the puzzle
def calculateCost(mat, final) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] and (mat[i][j] != final[i][j]):  # Check if the tile is not empty and is not in its final position
                count += 1  # Increment the count
    return count

# Function to create a new node by moving the empty tile
def newNode(mat, empty_tile_pos, new_empty_tile_pos, level, parent, final) -> node:
    new_mat = copy.deepcopy(mat)  # Deep copy the puzzle configuration
    x1, y1 = empty_tile_pos
    x2, y2 = new_empty_tile_pos
    # Swap the positions of the empty tile and the new position
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
    # Calculate the cost of the new node
    cost = calculateCost(new_mat, final)
    # Create and return the new node
    new_node = node(parent, new_mat, new_empty_tile_pos, cost, level)
    return new_node

# Function to print the puzzle configuration
def printMatrix(mat):
    for i in range(n):
        for j in range(n):
            print("%d " % (mat[i][j]), end=" ")  # Print each element of the puzzle
        print()

# Function to check if a given position is within the puzzle boundaries
def isSafe(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

# Function to print the path from the initial state to the final state
def printPath(root):
    if root == None:
        return
    printPath(root.parent)  # Recursively print the path
    printMatrix(root.mat)  # Print the puzzle configuration
    print()

# Function to solve the puzzle
def solve(initial, empty_tile_pos, final):
    pq = priorityQueue()  # Initialize priority queue
    cost = calculateCost(initial, final)  # Calculate the cost of the initial state
    # Create the root node
    root = node(None, initial, empty_tile_pos, cost, 0)
    pq.push(root)  # Push the root node into the priority queue
    while not pq.empty():  # While the priority queue is not empty
        minimum = pq.pop()  # Pop the node with the minimum cost
        if minimum.cost == 0:  # If the cost is 0, solution found
            printPath(minimum)  # Print the path to the solution
            return
        # Generate child nodes by moving the empty tile in all possible directions
        for i in range(n):
            new_tile_pos = [minimum.empty_tile_pos[0] + row[i], minimum.empty_tile_pos[1] + col[i]]
            if isSafe(new_tile_pos[0], new_tile_pos[1]):  # Check if the new position is valid
                # Create a new node for the child
                child = newNode(minimum.mat, minimum.empty_tile_pos, new_tile_pos, minimum.level + 1, minimum, final)
                pq.push(child)  # Push the child node into the priority queue

# Initial and final states of the puzzle, and the position of the empty tile
initial = [[1, 2, 3],
           [5, 6, 0],
           [7, 8, 4]]

final = [[1, 2, 3],
         [5, 8, 6],
         [0, 7, 4]]

empty_tile_pos = [1, 2]

# Solve the puzzle
solve(initial, empty_tile_pos, final)
