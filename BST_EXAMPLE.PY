class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def insert_BST(root, node):
    if root is None:
        root = node
        return
    if root.val < node.val:
        if root.right is None:
            root.right = node
        else:
            insert_BST(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert_BST(root.left, node)

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)
        
def delete_node_with_val(root, val):
    if root is None:
        return root
    if val < root.val:
        root.left = delete_node_with_val(root.left, val)
    elif val > root.val:
        root.right = delete_node_with_val(root.right, val)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = find_min_value_node(root.right)
        root.val = temp.val
        root.right = delete_node_with_val(root.right, temp.val)
    return root

def find_min_value_node(node):
    current = node
    while (current.left is not None):
        current = current.left
    return current

# Driver Code:
root = Node(6)
insert_BST(root, Node(8))
insert_BST(root, Node(2))
insert_BST(root, Node(5))
insert_BST(root, Node(4))
insert_BST(root, Node(9))
print("In-order traversal:")
in_order_traversal(root)
print("In-order traversal after deleting:")
root = delete_node_with_val(root, 2)
in_order_traversal(root)