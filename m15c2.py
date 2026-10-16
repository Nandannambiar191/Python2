# A graph data structure using adjacency list

class Graph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[i] for i in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def print_graph(self):
        for i in range(self.num_vertices):
            print(i, "->", self.adj_list[i])

# Create a graph with 5 vertices
g = Graph(5)

# Add edges between vertices 0 and 1, 0 and 2, 1 and 2, 2 and 3, 3 and 4
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

# Print the graph
g.print_graph()

"""--------------------------------------------------------------------------------"""

# A Python program to demonstrate the adjacency
# list representation of the graph

# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Add dest to src's list
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Add src to dest's list (undirected graph)
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}:\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print("\n")

# Driver code (to show output)
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()