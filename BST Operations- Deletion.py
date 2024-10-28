"""
Deletion: Deleting a node can be a bit tricky because you must maintain
the BST property even after the deletion. A node can be deleted following these steps:
If the node is a leaf node, delete the node outright.
If the node has only one child: Replace the node with its subtree.
If the node has both children: Find its in-order successor
 (the smallest value in its right subtree) or its in-order predecessor
 (the largest value in its left subtree) and replace the node with that value
 After replacing, delete the in-order successor or predecessor node.
"""
def minValueNode(node):
    # This function finds the node with the smallest value in a BST
    current = node
    
    # The smallest value is located at the leftmost leaf.
    # Therefore, we iterate until the left child node is None
    while (current.left is not None):
        current = current.left
    return current

def deleteNode(root, key):
    # This function deletes the node containing the value key from the BST

    # If the root is None, then the tree is empty.
    # Therefore, we return the root
    if root is None:
        return root
    
    # The value key is less than the root's value, then it lies in the left subtree
    if key < root.val:
        root.left = deleteNode(root.left, key)
    # The value key is greater than the root's value, then it lies in the right subtree
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # If the key is equal to the root's key, then this is the node to be deleted

        # If a node with only one child or no child,
        # the root's right child replaces the root if the left child does not exist
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        # If node has two children, get the inorder successor (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's content to this node
        root.val = temp.val

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.val)

    return root