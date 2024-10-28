from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        result = []
        window = deque()  # Store indices of the elements
        
        for r in range(len(nums)):
            # Remove elements from the deque that are out of the current window
            if window and window[0] < r - k + 1:
                window.popleft()

            # Remove elements from the deque that are smaller than the current element
            # because they will not be the maximum when the current element is in the window
            while window and nums[window[-1]] <= nums[r]:
                window.pop()

            # Add the current element's index to the deque
            window.append(r)

            # Once the window is of size k, add the current maximum (the front of the deque) to the result
            if r >= k - 1:
                result.append(nums[window[0]])

        return result