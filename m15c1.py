class Graph:

    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, node1, node2, weight=1):
        if node1 not in self.nodes:
            self.nodes.add(node1)
        if node2 not in self.nodes:
            self.nodes.add(node2)

        if node1 not in self.edges:
            self.edges[node1] = set()
        self.edges[node1].add((node2, weight))

        if node2 not in self.edges:
            self.edges[node2] = set()
        self.edges[node2].add((node1, weight))

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def __repr__(self):
        return str(self.nodes) + " -> " + str(self.edges)

# Create a graph
graph = Graph()

# Add nodes
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")

# Add edges
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")

# Print the graph
print(graph)


"""--------------------------------------------------------------------"""

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adjacency_matrix = [[0 for i in range(num_nodes)] for j in range(num_nodes)]

    def add_edge(self, node1, node2, weight=1):
        self.adjacency_matrix[node1][node2] = weight
        self.adjacency_matrix[node2][node1] = weight

    def get_nodes(self):
        return range(self.num_nodes)

    def get_edges(self):
        edges = []
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                if self.adjacency_matrix[i][j] != 0:
                    edges.append((i, j))
        return edges

    def __repr__(self):
        return str(self.adjacency_matrix)

# Create a graph
graph = Graph(3)

# Add edges
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)

# Print the graph
print(graph)