def kthSmallest(root, k):
    # The number of nodes in the left subtree of the root
    left_nodes = countNodes(root.left) if root else 0
    
    # If k is equal to the number of nodes in the left subtree plus 1, 
    # That means we must return the root's value as we've reached the k-th smallest
    if k == left_nodes + 1:
        return root.val
    # If there are more than k nodes in the left subtree,
    # The k-th smallest must be in the left subtree.
    elif k <= left_nodes:
        return kthSmallest(root.left, k)
    # If there are less than k nodes in the left subtree,
    # The k-th smallest must be in the right subtree.
    else:
        return kthSmallest(root.right, k - 1 - left_nodes) 

def countNodes(root):
    if not root:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)