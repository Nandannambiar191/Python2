def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start, end=" ")
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS Traversal:")
dfs(graph, 'A')


"""--------------------------------------------------------------------------"""

def dfs(graph, start):
    """
    Performs a depth-first search on the given graph, starting at the given node.

    Args:
    graph: The graph to search.
    start: The node to start the search at.

    Returns:
    A list of the nodes visited by the search, in the order in which they were visited.
    """

    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(neighbor)

    return visited
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

visited = dfs(graph, 'A')

print(visited)