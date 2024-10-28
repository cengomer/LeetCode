# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):    
    def mergeKLists(self, lists):
        stack = []
        # Traverse the given lists
        for l in lists:
            current = l
            while current:
                stack.append(current.val)  # Use `val` to access the value in ListNode
                current = current.next
        # Sort the stack in ascending order
        stack.sort()
        # Create a new sorted linked list from the sorted stack
        dummy = ListNode(0)
        current = dummy
        for value in stack:
            current.next = ListNode(value)
            current = current.next
        return dummy.next