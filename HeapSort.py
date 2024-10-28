def heap_sort(arr):
    import heapq
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

print(heap_sort([1,4,673,1,46,5,456,23,55,2,7,8,4,6,2]))
#simply its make our array sorted !