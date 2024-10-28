class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # If the target amount is 0, no coins are needed.
        if amount == 0:
            return 0

        # Initialize a dp array where dp[i] holds the minimum number of coins needed to make amount i.
        # Set the values to infinity because we will be looking for the minimum, except dp[0] = 0.
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # Iterate over each amount from 1 to the target amount.
        for i in range(1, amount + 1):
            # For each amount i, check every coin in the coins list.
            for coin in coins:
                # If the current amount i is greater than or equal to the coin value, we can use this coin.
                if i - coin >= 0:
                    # Update dp[i] to the minimum of its current value or using this coin (dp[i - coin] + 1).
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still infinity, it means no solution was found, so return -1.
        # Otherwise, return dp[amount], the fewest number of coins needed.
        return dp[amount] if dp[amount] != float('inf') else -1