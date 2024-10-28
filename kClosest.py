import heapq
class Solution(object):
    def kClosest(self, points, k):
        min_heap = []
        heapq.heapify(min_heap)

        for idx, val in enumerate(points):
            first,last = val
            result = -((first ** 2) + (last ** 2))
            heapq.heappush(min_heap, (result, idx))

            while len(min_heap) > k:
                heapq.heappop(min_heap)   

        return [points[idx] for _, idx in min_heap]
