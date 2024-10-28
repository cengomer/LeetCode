import heapq

class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)  # Turn the nums list into a heap
        while len(self.nums) > k:  # Keep only the largest k elements
            heapq.heappop(self.nums)

    def add(self, val):
        heapq.heappush(self.nums, val)  # Add the new value to the heap
        if len(self.nums) > self.k:  # If the heap size exceeds k, pop the smallest
            heapq.heappop(self.nums)
        return self.nums[0]  # The kth largest is the smallest element in the heap