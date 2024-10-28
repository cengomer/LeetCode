class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def find_sum(head):
    prev = None 
    current = head
    stack = []
    while head is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        
    sum_  = 0
    index = 1
    while prev is not None:
        if index % 3 == 0:
            sum_ += prev.data
        prev = prev.next
        index += 1
    return sum_
        