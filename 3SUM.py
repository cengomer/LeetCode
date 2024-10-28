class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()  # Sorting is good
        
        for i in range(len(nums)):  # FIXED: Correct, loop through indices now
            if i > 0 and nums[i] == nums[i-1]:  # ADD: This skips duplicate values for i
                continue
            
            left = i + 1  # FIXED: Correct initialization of left
            right = len(nums) - 1  # Right is correctly initialized
            
            first_element = nums[i]  # FIX: You're now using the correct first element
            
            while left < right:  # Correct while loop for two-pointer logic
                total = nums[left] + nums[right] + first_element
                
                if total == 0:  # If the triplet sums to zero, append it
                    result.append([nums[left], nums[right], first_element])
                    
                    # ADD: Move pointers and skip duplicates to avoid repeating triplets
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1  # Move left after finding a valid triplet
                    right -= 1  # Move right after finding a valid triplet
                
                elif total < 0:  # If the sum is too small, move the left pointer to the right
                    left += 1
                else:  # If the sum is too large, move the right pointer to the left
                    right -= 1

        return result