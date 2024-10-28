graph = {
    'Washington': set(['California', 'Nevada']),
    'California': set(['Washington', 'Oregon']),
    'Nevada': set(['Washington', 'Oregon']),
    'Oregon': set(['California', 'Nevada'])
}

def DFS(graph, start, visited):
    if start in visited:  # if the node has already been visited, just return the visited set
        return
   
    visited.add(start)
    print(start, end=" ")

    for state in graph[start]:
        if state not in visited:
            DFS(graph, state, visited)

# Call the DFS function starting with 'Washington'
visited = set()
DFS(graph, 'Washington', visited)  # Output: Washington Nevada Oregon California
print('\nVisited states:', visited)  # Print all visited states