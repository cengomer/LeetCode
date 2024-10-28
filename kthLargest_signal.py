import heapq
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthLargest(root, k):
    min_heap = []
    
    def traverse(node):
        if not node:
            return
        # Traverse the left subtree
        traverse(node.left)
        # Traverse the right subtree
        traverse(node.right)
        # Push the current node's value into the heap
        heapq.heappush(min_heap, node.val)
        # If heap size exceeds k, remove the smallest element
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    traverse(root)
    
    # The root of the min-heap is the k-th largest element
    return min_heap[0] if min_heap else None
    
    
# Creating the BST
root = Node(50) 
root.left = Node(20)
root.right = Node(60) 
root.left.left = Node(10) 
root.left.right = Node(30)
root.right.left = Node(55)
root.right.right = Node(70)
root.left.right.left = Node(25)
root.left.right.right = Node(35)
root.right.right.left = Node(65)
root.right.right.right = Node(80)

# Now, let's test the function with the new binary tree
print(kthLargest(root, 1))  # Expected output: 80
print(kthLargest(root, 5))  # Expected output: 55
print(kthLargest(root, 10))  # Expected output: 20
print(kthLargest(root, 3))  # Expected output: 65
print(kthLargest(root, 7))  # Expected output: 35