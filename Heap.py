"""
What are Heaps?
A heap is a complete binary tree that satisfies a 
special property known as the heap property.
Essentially, the heap property stipulates that if P is a parent node of C,
the value of node P is either greater than or equal to (in the case of a Max Heap)
or lesser than or equal to (in a Min Heap) the value of node C.
In simpler terms, in a Max Heap,
each parent node is greater than or equal to its child node(s),
and in a Min Heap, each parent node is less than or equal to its child node(s).


Heap Operations
Heaps support numerous operations, such as:
1. Insert: Inserting a new node in a heap may disrupt the heap property. To maintain the heap property after each insertion, the node is swapped with the parent node if the heap property is violated. This process continues until the heap property is retained for all nodes.
2. Delete: The deletion of a node also disrupts the heap property. After deleting a node, the heap property is restored either by swapping the node with its parent, similar to the Insert operation or by swapping it with one of its children. The swapping process continues until the heap property is retained for all nodes.
3. Extract: Extracting the maximum (for Max Heap) or minimum (for Min Heap) is a constant-time operation, as the maximum or the minimum element is always at the root of the heap.
"""