class Solution(object):
    def findMin(self, nums):
        low = 0
        high = len(nums) - 1

        while high - low > 1:
            mid = (high + low) // 2
            if nums[mid] < nums[-1] :
                # then from mid to high is the sorted part ?
                high = mid
            else:
                low = mid
        return nums[low] if nums[low] < nums[high] else nums[high]