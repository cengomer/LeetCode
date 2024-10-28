import heapq

heap = []

heapq.heappush(heap,4)
heapq.heappush(heap,9)
heapq.heappush(heap,6)

print("Heap after Insertion: ", heap)

heapq.heappop(heap)
print("heap after deletion: ", heap)

smallest = heapq.nsmallest(1,heap)[0]
print("Smallest element in the heap: ", smallest)

"""
In the given snippet, the heappush(heap, ele) 
function is used to insert elements while maintaining the heap invariant,
 heappop(heap) function deletes the smallest element, and the nsmallest(n, iterable[, key]) function returns n smallest elements from the iterable or heap.


"""
