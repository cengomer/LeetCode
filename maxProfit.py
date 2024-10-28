class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = 0  # Left pointer for the buying day
        max_profit = 0  # Initialize maximum profit to 0
        
        # Iterate with right pointer from day 1 to the end
        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                # Calculate the profit if selling on day r
                profit = prices[r] - prices[l]
                # Update max profit
                max_profit = max(max_profit, profit)
            else:
                # If prices[r] is less or equal, move the buying day to r
                l = r
        
        return max_profit