class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If total sum is odd, can't partition into two equal subsets
        if total_sum % 2 != 0:
            return False

        # Target sum for each subset
        target = total_sum // 2
        
        # DP array where dp[i] is True if subset sum i can be formed
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: subset sum 0 can always be formed (empty set)
        
        # Iterate through each number in nums
        for num in nums:
            # Update dp array from target down to num (backwards)
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        # Final result: Can we form a subset with sum equal to target?
        return dp[target]