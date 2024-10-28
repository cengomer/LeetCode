class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def add_edges(tree, node, child_values):
    for value in child_values:
        node.children.append(Node(value))

def dfs(node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node.value)
    print(node.value, end=' -> ')

    for child in node.children:
        if child.value not in visited:
            dfs(child, visited)

# Constructing a tree
root = Node('Head Office')
add_edges(root, root, ['Marketing', 'Sales', 'R&D'])

node_marketing = root.children[0]
add_edges(root, node_marketing, ['SEO', 'Content'])

node_sales = root.children[1]
add_edges(root, node_sales, ['Domestic', 'International'])

# Perform DFS traversal
print("DFS Traversal:")
dfs(root)
print("end")