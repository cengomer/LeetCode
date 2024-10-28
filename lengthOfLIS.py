from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        lis = []
        
        for num in nums:
            pos = bisect_left(lis, num)  # Find the insertion position
            
            # If pos is equal to the length of lis, num is greater than all elements
            if pos == len(lis):
                lis.append(num)  # Extend the list
            else:
                lis[pos] = num  # Replace the found position
        
        return len(lis)  # The length of the longest increasing subsequence
