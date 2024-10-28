# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.max_sum = float('-Inf')
        def dfs(node):
            if not node:
                return 0
            
            left  = max(dfs(node.left),0)
            right = max(dfs(node.right) , 0)

            curr_sum = node.val + left + right

            self.max_sum = max(self.max_sum,curr_sum)

            return node.val + max(left,right)
        dfs(root)
        return self.max_sum
        