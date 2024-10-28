class Solution:
    def numDecodings(self , s: str) -> int:
        # Edge case: If the string starts with '0', no valid decodings are possible
        if not s or s[0] == '0':
            return 0

        n = len(s)
        # dp array to store the number of ways to decode up to each index
        dp = [0] * (n + 1)
        
        # Base case: There's one way to decode an empty string
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        # Fill dp array
        for i in range(2, n + 1):
            # Check if the single digit at position i-1 is valid
            if 1 <= int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            
            # Check if the two digits at position i-2 to i-1 are valid
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]
