"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):

        if not head:
            return None

        old_to_new = {}
        iterate = head

        while iterate:
            old_to_new[iterate] = Node(iterate.val)
            iterate = iterate.next

        iterate = head

        while iterate: 
            if iterate.next != None:
                old_to_new[iterate].next = old_to_new[iterate.next]

            if iterate.random != None:
                old_to_new[iterate].random = old_to_new[iterate.random]
            
            iterate = iterate.next
        
        return old_to_new[head]