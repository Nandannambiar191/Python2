# A utility function to add an 
# edge in an undirected graph.
def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

# A utility function to do DFS of graph
# recursively from a given vertex u.
def DFSUtil(u, adj, visited):
    visited[u] = True
    for i in range(len(adj[u])):
        if (visited[adj[u][i]] == False):
            DFSUtil(adj[u][i], adj, visited)

# Returns count of tree is the 
# forest given as adjacency list.
def countTrees(adj, V):
    visited = [False] * V
    res = 0
    for u in range(V):
        if (visited[u] == False):
            DFSUtil(u, adj, visited)
            res += 1
    return res

# Driver code
if __name__ == '__main__':
    V = 5
    adj = [[] for i in range(V)]
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 0, 3)
    addEdge(adj, 3, 4)
    print(countTrees(adj, V))

"""--------------------------------------------------------------------------"""

# Python program for the above approach

# Function to find the minimum
# number of rabbits in the forest
def minNumberOfRabbits(answers, N):
    # initialize map
    Map = {}
    
    # Traverse array answers[] 
    # to the number of occurrences
    for a in range(N):
        if answers[a] in Map:
            Map[answers[a]] += 1
        else:
            Map[answers[a]] = 1
    
    # Initialize count
    count = 0
    
    # Find the rabbit groups and 
    # no. of rabbits in each group
    for a in Map:
        x = a
        y = Map[a]
        
        # Find number of groups and 
        # multiply them with number 
        # of rabbits in each group
        if (y % (x + 1)) == 0:
            count = count + ((y // (x + 1)) * (x + 1))
        else:
            count = count + ((y // (x + 1) + 1) * (x + 1))
    
    # count gives minimum number 
    # of rabbits in the forest
    return count

# Driver code
arr = [2, 2, 0, 0]
N = len(arr)

# Function Call
print(minNumberOfRabbits(arr, N))