"""
Searching will help us find if a value exists in the BST.
We start at the root and traverse down the tree until we find the key.
If the key's value is greater than a node's value, we move right, and if it's smaller,
we move left. If we can't locate the key or the tree is empty, our function returns None,
indicating that the key is not present in the BST.
"""
def search(root, key): 
    if root is None or root.val == key: 
        return root 
    if root.val < key: 
        return search(root.right, key) 
    return search(root.left, key)