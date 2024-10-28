def find_path(tree , start , end , visited , path=[]):
    path = path + [start]
    visited.add(start)
    if start == end:
        return path
    for node in tree[start]:
        if node not in visited:
            new_path = find_path(tree,node,end,visited,path)
            if new_path:
                return new_path
    return None

visited = set()
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

print(find_path(tree, 'A' ,'J',visited))