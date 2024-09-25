def dfs(graph, vertex, visited):
    # Mark the current vertex as visited
    visited.add(vertex)
    print(vertex, end=' ')  # Print the vertex during the traversal
    
    # Recursively visit all the adjacent vertices
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()  
start_vertex = 'A'  
print("DFS Traversal starting from vertex", start_vertex)
dfs(graph, start_vertex, visited)
