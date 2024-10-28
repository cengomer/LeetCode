# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []

        visited = []
        queue = deque()
        queue.append(root)

        while queue:
            tempList = []
            level_length = len(queue)

            for _ in range(level_length):
                curr = queue.popleft()
                tempList.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            visited.append(tempList)           
        return visited
