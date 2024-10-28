class Node: 
    def __init__(self, value):
        self.value = value 
        self.next  = None

class LinkedList: 
    def __init__(self):
        self.head = None 
        self.tail = None

    def insert(self,value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        """
The delete() method begins by setting a temp reference
to the head of the linked list. This temp reference will be used to traverse the list.
        """
    def delete(self,value): 
        temp = self.head
        if (temp is not None):
            if temp.value == value:
                self.head = temp.next
                temp = None
                return
            
        while (temp is not None):
            if temp.value == value:
                break
            prev = temp
            temp = temp.next
    
        if temp == None: 
            return
        prev.next = temp.next
        temp = None
    

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value,end=" => ")
            temp = temp.next
                
list = LinkedList()
list.insert(1)
list.insert(2)
list.insert(3)
list.print() # Output: 1 => 2 => 3 =>
list.delete(2)
list.print() # Output: 1 => 3 =>
"""
Diving Deep into Linked List Manipulation
In order to understand and use linked lists effectively, we need to master certain operations such as insertion, deletion, and traversal. Let's break each one down:
Insertion: When we talk about insertion, we are referring to the process of adding a new node to the existing list.
Deletion: Contrarily, deletion describes the action of removing a specific node from the list.
Traversal: This operation is involved with accessing and scanning through the elements in the list, one by one.
For our discussion, let's use Python to create a small class-based implementation of a linked list. Following this structure, we can effectively understand and manipulate situated nodes in a linked list.
Let's discuss the methods of the LinkedList class in more detail.
"""