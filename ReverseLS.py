class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None

    def LinkedList_reverseTraversal(self):
        node = self.head
        stack = []
        while node is not None:
            stack.append(node.data)
            node = node.next
        while stack:
            print(stack.pop())