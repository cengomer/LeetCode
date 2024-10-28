# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def kthSmallest(self, root, k):
        # Helper function for in-order traversal
        def in_order_traversal(node):
            if not node:
                return []
            # Traverse left subtree, then root, then right subtree
            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
        
        # Perform in-order traversal of the tree and get sorted elements
        sorted_elements = in_order_traversal(root)
        # Return the k-th smallest element
        return sorted_elements[k-1]