# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if root is None:
            return False
        
        # Check if the current tree matches the subRoot
        if self.isSameTree(root, subRoot):
            return True
        
        # Recur on the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        
        # Check if current nodes are equal and recur for left and right children
        return (s.val == t.val) and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)