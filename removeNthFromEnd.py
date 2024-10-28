# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        curr = head
        stack = []

        while curr:
            stack.append(curr.val)
            curr = curr.next

        index = -n
        if -len(stack) <= index < len(stack):
            stack.pop(index)
        head = None
        while stack:
            val = stack.pop()
            new_nod = ListNode(val)
            new_nod.next = head
            head = new_nod
        return head