"""
Insertion: To maintain the key BST property during insertion,
a new value x must be carefully positioned. We start at the root and traverse down the BST.
If x is less than the current node's value, we go left; if it's greater, we move to the right
child. We continue this movement until we find an appropriate spot devoid of a child node
where we place x in a new node at that location.
"""
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val  < key : 
            root.right = insert(root.right , key)
        else:
            root.left = insert(root.left,key)
    return root