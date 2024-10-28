import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        # Convert stones to a max-heap by inserting negative weights
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            # Pop the two heaviest stones
            first = heapq.heappop(max_heap)  # Heaviest
            second = heapq.heappop(max_heap) # Second heaviest
            
            if first != second:
                # If they are not equal, push the difference back into the heap
                # Since we're using negative numbers, we add them
                heapq.heappush(max_heap, first - second)
            # If they are equal, both stones are destroyed (do nothing)
        
        # If there's a stone left, return its weight (convert back to positive)
        # Otherwise, return 0
        return -max_heap[0] if max_heap else 0
