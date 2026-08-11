#Brian Doyle
# 4/13/26
# In this graph lab I will be building out the graph class that we were given
# This class can do four things. It can search a graph using BFS, DFS, Topological Sort and Dijkstra's algorithm. All these algorithms have a great impact on the real world.
# Helping to create things like gps, google maps, and help in the devoploment of AI.

import heapq
from multiprocessing import heap


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.vertices = []  # list of vertices
        self.adj = {}  # dict: map vertex to adj list
        # Todo: add additional data members, for BFS, DFS
        self.d = {}
        self.pred = {}
        self.color = {}
        self.post_order = []
        self.post_order_color = []
        self.weights = {}

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices.append(v)
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v, weight=None):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        if weight is not None:
            self.weights[(u, v)] = weight
        if not self.directed:
            self.adj[v].append(u)
            if weight is not None:
                self.weights[(v, u)] = weight

    def initialize_from_file(self, file_name):
        print(f"Loading graph from {file_name}")
        self.vertices = []
        self.adj = {}

        try:
            f = open(file_name, "r")
        except IOError:
            print(f"Failed to open file {file_name}")
            raise

        # Read directed flag
        word = f.readline().strip()
        if word.lower() == "true":
            self.directed = True
        elif word.lower() == "false":
            self.directed = False
        else:
            raise ValueError(f"Invalid directed flag: {word}")

        print(f"The graph is directed: {word}")

        # Read number of nodes
        line = f.readline().strip()
        node_num = int(line)
        print(f"With {node_num} nodes")

        # Read node list and initialize adjacency lists
        nodes = f.readline().split()
        for u in nodes:
            self.add_vertex(u)

        # Read edges of the form: "u label v"
        for line in f:
            parts = line.split()
            if len(parts) != 3:
                continue
            from_node, label, to_node = parts
            self.add_edge(from_node, to_node)

        f.close()

    def print(self):
        print("Vertices:")
        print(self.vertices)

        print("Adjacency lists:")
        # Iterate through all key value pair in the dict adj:
        for u, adjList in self.adj.items():
            print("Node ", u, "'s adjacency list:")
            print(adjList)

    def BFS(self, s):
        print("Perform a BFS from src node", s)
        # Todo by you
        print("Perform a DFS from src node", s)
        visited = set()
        visited.add(s)
        self.d = {}
        self.pred = {}
        self.d[s] = 0
        self.pred[s] = None
        Q = [s]
        while Q:
            u = Q.pop(0)
            for v in self.adj[u]:
                if v not in visited:
                    self.d[v] = self.d[u] + 1
                    self.pred[v] = u
                    visited.add(v)
                    Q.append(v)
        print("d[]  =", self.d)
        print("pred[] =", self.pred)

    def ShortestHopPath(self, s, d):
        print("Find shortest hop path from ", s, "to ", d)
        # todo by you
        self.BFS(s)
        if d not in self.pred and d != s:
            print(f"No path from {s} to {d}")
            return []
        path = []
        node = d
        while node is not None:
            path.append(node)
            node = self.pred.get(node)
        path.reverse()
        if path[0] != s:
            print(f"No path from {s} to {d}")
            return []
        print("Shortest hop path", path)
        return path
    # helper function that will help DFS and DFS_Graph with recursion
    def dfs_visit(self, u, visited):
        visited.add(u)
        self.pre_order.append(u)
        self.color[u] = "gray"
        for v in self.adj[u]:
            if v not in visited:
                self.pred[v] = u
                self.dfs_visit(v, visited)
        self.color[u] = "black"
        self.post_order.append(u)

    def DFS(self, s):
        print("Perform a DFS from src node", s)
        # todo by you
        self.pre_order = []
        self.post_order = []
        self.color = {v: "White" for v in self.vertices}
        self.pred = {v: None for v in self.vertices}
        visited = set()
        self.dfs_visit(s, visited)
        print("pre_order[] =", self.pre_order)
        print("post_order[] =", self.post_order)

    def DFS_Graph(self):
        print("Perform a complete DFS")
        # Initialize color dictionary , visited set, pre-order list
        # and post-order list
        # todo by you
        # full traversal of the graph
        print("Perform a complete DFS")
        self.pre_order = []
        self.post_order = []
        self.color = {v: "white" for v in self.vertices}
        self.pred = {v: None for v in self.vertices}
        visited = set()
        for v in self.vertices:
            if v not in visited:
                self.dfs_visit(v, visited)
        print("pre_order[] =", self.pre_order)
        print("post_order[] =", self.post_order)

    # DAG Helper function this function will be called by Dag_Topsort
    def dfs_topo(self, u, color, topo_stack):
        color[u] = "gray"
        for v in self.adj[u]:
            if color[v] == "gray":
                # cycle found
                return True
            if color[v] == "white":
                if self.dfs_topo(v, color, topo_stack):
                    return True
        color[u] = "black"
        topo_stack.append(u)
        return False

    def DAG_TopoSort(self):
        print("DAG: cycle detection, topological sort")
        # Initialize color dictionary , visited set
        # todo by you
        print("Dag: cycle detection, topological sort")
        color = {v: "white" for v in self.vertices}
        topo_stack = []
        for v in self.vertices:
            if color[v] == "white":
                if self.dfs_topo(v, color, topo_stack):
                    print("Graph has a cycle topological sort is not possible")
                    return None
        topo_order = list(reversed(topo_stack))
        print("Topological order:", topo_order)
        return topo_order

# Extra credit
# implementation of Dijkstra algortithm
def Dijkstra(self,s):
        print("Dijkstra algorithm")
        for (u, v), w in self.weights.items():
            if w < 0:
                raise ValueError(
                    f"Dijkstra requires non-negative weights,"
                    f"but edge ({u},{v}) has weight {w}"
                )
        # set each nodes distance to be inrinity at the start.
        INF = float("inf")
        self.d = {v: INF for v in self.vertices}
        self.pred = {v: None for v in self.vertices}
        self.d[s] = 0
        visited = set()
        while heap:
            dist_u, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            for v in self.adj[u]:
                w = self.weights.get((u, v), 1)
                if self.d[v] + w < self.d[u]:
                    self.d[v] = self.d[u] + w
                    self.pred[v] = u
                    heapq.heappush(heap, (self.d[v], v))
            print("dist[]", self.d)
            print("pred[]", self.pred)

# Finding the shortest weighted path
def Shortweightedpath(self, s, d):
    self.Dijkstra(s)
    print(f"Shortest weighted path from {s} to {d}")
    if self.d[d] == float("inf"):
        print(f"No path from {s} to {d}")
        return []
    path = []
    node = d
    while node is not None:
        path.append(node)
        node = self.pred[node]
    path.reverse()
    print(f" Path: {path}")
    print(f"Cost: {self.d[d]}")
    return path


# Example usage
if __name__ == "__main__":
    g = Graph(directed=False)
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "C")
    g.add_edge("C", "D")

    g.print()

    g1 = Graph()
    g1.initialize_from_file("dressing.txt")
    g1.print()

    g2 = Graph(directed=False)
    g2.initialize_from_file("undirected_graph.txt")
    g2.print()

    # Todo #1 Test BFS on g2 using node B as source node
    # print out the d[], and pred[] dict after BFS()
    g2.BFS("B")

    # Todo #2: Find shortest hop path in g1 from one node to another
    g1.ShortestHopPath("shirt", "jacket")

    # Todo #3: test DFS_Graph on g1, print the pre-order and post-order
    g1.DFS_Graph()

    # Todo #4: test DFS_TopoSort on g2, print the topological order
    g1.DAG_TopoSort()


    # Todo #5: add an edge to g2 to make it cyclic, and test DFS_TopoSort on g2,
    #  it should report there is a cycle
    g2.add_edge("D", "A")
    g2.DAG_TopoSort()

    # Todo #6: test DFS_TopoSort
    g2.DAG_TopoSort()

    # Test Dijkstra on the weighted graph
    wg = Graph(directed=True)
    wg.add_edge("A", "B", 4)
    wg.add_edge("A", "C", 2)
    wg.add_edge("C", "B", 1)
    wg.add_edge("B", "D", 5)
    wg.add_edge("C", "D", 8)
    wg.add_edge("D", "E", 2)
    wg.add_edge("B", "E", 6)
    wg.ShortestHopPath("A", "E")
