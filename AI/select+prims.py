class Graph:
    def __init__(self, vertices):
        # Initialize the graph with given number of vertices
        self.V = vertices
        # Create a 2D array to represent the graph with all edges initially set to 0
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        # Add an edge between vertices u and v with given weight
        # Since it's an undirected graph, we set the weight for both u->v and v->u
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def print_mst(self, parent):
        # Print the edges and their weights in the Minimum Spanning Tree (MST)
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def min_key(self, key, mst_set):
        # Find the vertex with the minimum key value from the set of vertices not yet included in MST
        min_value = float('inf')  # Initialize minimum value as infinity
        min_index = -1  # Initialize index of minimum value
        for v in range(self.V):
            # If vertex v has not been included in MST and its key value is smaller than current minimum value
            if key[v] < min_value and not mst_set[v]:
                min_value = key[v]  # Update minimum value
                min_index = v  # Update index of minimum value
        return min_index

    def prim_mst(self):
        # Function to construct and print MST using Prim's algorithm
        key = [float('inf')] * self.V  # Initialize key values as infinity
        parent = [-1] * self.V  # Initialize parent array to store MST
        key[0] = 0  # Set key value of first vertex to 0 to include it in MST
        mst_set = [False] * self.V  # Initialize set to keep track of vertices included in MST

        for _ in range(self.V):
            u = self.min_key(key, mst_set)  # Get the vertex with minimum key value not yet included in MST
            mst_set[u] = True  # Include vertex u in MST
            for v in range(self.V):
                # Update key value and parent index of adjacent vertices of u if they are not yet included in MST
                if 0 < self.graph[u][v] < key[v] and not mst_set[v]:
                    key[v] = self.graph[u][v]  # Update key value of vertex v
                    parent[v] = u  # Update parent index of vertex v

        self.print_mst(parent)  # Print the constructed MST


def selection_sort(arr):
    # Function to perform selection sort on an array
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the minimum element with the current element
    return arr


if __name__ == "__main__":
    # Main function
    print("Selection Sort:")
    arr = list(map(int, input("Enter space-separated integers for array: ").split()))
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)

    print("\nPrim's Minimal Spanning Tree Algorithm:")
    vertices = int(input("Enter the number of vertices in the graph: "))
    g = Graph(vertices)  # Create a graph object with given number of vertices
    edges = int(input("Enter the number of edges in the graph: "))
    print("Enter edges in the format 'source destination weight':")
    for _ in range(edges):
        # Add edges to the graph
        u, v, weight = map(int, input().split())
        g.add_edge(u, v, weight)
    g.prim_mst()  # Find and print Minimum Spanning Tree using Prim's algorithm

"""Prim's Minimal Spanning Tree Algorithm:
Enter the number of vertices in the graph: 9
Enter the number of edges in the graph: 14
Enter edges in the format 'source destination weight':
0 1 4
1 2 8
2 3 7
3 4 9
4 5 10
5 6 2
6 7 1
7 0 8
1 7 11
2 8 2
8 6 6
3 5 15
7 8 7
2 5 4
"""
