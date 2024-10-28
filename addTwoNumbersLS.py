# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)  # Dummy node to simplify result construction
        current = dummy_head  # Pointer to the current node in the result list
        carry = 0  # To keep track of the carry from sum

        # Traverse both linked lists until both are exhausted
        while l1 or l2 or carry:
            # Get the values from the current nodes, or 0 if a list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of the current digits + carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10  # Update carry for the next iteration
            new_digit = total_sum % 10  # This is the digit to store in the new node

            # Create a new node with the sum's last digit and move the pointer
            current.next = ListNode(new_digit)
            current = current.next

            # Move to the next nodes in l1 and l2 (if they exist)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next  # The result starts at dummy_head.next