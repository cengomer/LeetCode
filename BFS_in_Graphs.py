from collections import  deque

def BFS(graph , start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node,end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

"""
This Python code demonstrates a BFS() function that accepts
a graph (presented as an adjacency list) and a starting point for the BFS traversal.
It uses a deque to handle BFS operations and a set visited to track visited nodes.
"""
