class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val 

root = Node(5)
root.left = Node(3)
root.right = Node(9)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(6)
