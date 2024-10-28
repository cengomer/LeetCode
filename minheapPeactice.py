# Import necessary libraries
import heapq

# Create an empty MinHeap
minHeap = []

# Function to insert nodes maintaining the heap property
def insertNode(node_list):
    for node in node_list:
        heapq.heappush(minHeap, node)

# Function to delete node from heap
def deleteNode():
    try:
        return heapq.heappop(minHeap)
    except:
        return None

# insert nodes into the MinHeap
insertNode([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

# print MinHeap after insertions
print("Heap after insertions: ", minHeap)

# Delete a node from MinHeap
deleteNode()

# print MinHeap after deletion
print("Heap after deleting the minimum node: ", minHeap)