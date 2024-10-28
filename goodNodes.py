# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def goodNodes(self, root):
        if root is None:
            return 0

        # Initialize queue with a tuple of (node, current maximum value)
        queue = deque([(root, root.val)])
        goodNodesNum = 0

        while queue:
            curr, curr_max = queue.popleft()

            if curr.val >= curr_max:
                goodNodesNum += 1

            # Update the max value when adding children to the queue
            if curr.left:
                queue.append((curr.left, max(curr_max, curr.left.val)))
            if curr.right:
                queue.append((curr.right, max(curr_max, curr.right.val)))

        return goodNodesNum
