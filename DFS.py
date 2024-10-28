def dfs(tree , root , visited , traversal):
    traversal.append(root)
    visited.add(root)


    for child in tree[root]:
        if child not in visited:
            dfs(tree,child,visited,traversal)

tree = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A'],
    'D': ['A', 'G', 'H'],
    'E': ['B'],
    'F': ['B', 'I', 'J'],
    'G': ['D'],
    'H': ['D'],
    'I': ['F'],
    'J': ['F'],
}

visited = set()
traversal = []
dfs(tree, 'A' , visited , traversal)
print(' -> '.join(traversal))