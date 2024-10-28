# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node and a pointer to build the new list
        dummy_head = ListNode()
        current = dummy_head
        
        # Traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If any nodes are left in list1 or list2, append them
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # Return the next of dummy node which is the head of the merged list
        return dummy_head.next