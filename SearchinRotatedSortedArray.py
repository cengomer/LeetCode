class Solution(object):
    def search(self, nums, target):
        low = 0 
        high = len(nums) - 1

        while low < high:
            mid = (high + low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1 
            else:
                high = mid
        pivot = low
        low = 0
        high = len(nums) - 1

        if target >= nums[pivot] and target <= nums[high]:
            low = pivot
        else:
            high = pivot - 1
        
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
 
