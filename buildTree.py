# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        hashMap = {val: idx for idx, val in enumerate(inorder)}
        
        def helperDefRecursion(preorderIndex, inorderStart, inorderEnd):
            if inorderStart > inorderEnd : 
                return None

            rootValue = preorder[preorderIndex]
            root = TreeNode(rootValue) 
            inorderIndex = hashMap[rootValue]
            root.left = helperDefRecursion(preorderIndex + 1, inorderStart, inorderIndex - 1)
            root.right = helperDefRecursion(preorderIndex + (inorderIndex - inorderStart + 1), inorderIndex + 1, inorderEnd)

            return root

        return helperDefRecursion(0, 0, len(inorder) - 1)
