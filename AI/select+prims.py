class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def min_key(self, key, mst_set):
        min_value = float('inf')
        min_index = -1
        for v in range(self.V):
            if key[v] < min_value and not mst_set[v]:
                min_value = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        key = [float('inf')] * self.V
        parent = [-1] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True
            for v in range(self.V):
                if 0 < self.graph[u][v] < key[v] and not mst_set[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    print("Selection Sort:")
    arr = list(map(int, input("Enter space-separated integers for array: ").split()))
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)

    print("\nPrim's Minimal Spanning Tree Algorithm:")
    vertices = int(input("Enter the number of vertices in the graph: "))
    g = Graph(vertices)
    edges = int(input("Enter the number of edges in the graph: "))
    print("Enter edges in the format 'source destination weight':")
    for _ in range(edges):
        u, v, weight = map(int, input().split())
        g.add_edge(u, v, weight)
    g.prim_mst()
