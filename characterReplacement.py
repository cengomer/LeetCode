class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        l = 0
        max_len = 0
        for r in range(len(s)):
            # Update the frequency count for the current character
            count[s[r]] = count.get(s[r], 0) + 1
            # Track the frequency of the most frequent character in the current window
            max_freq = max(max_freq, count[s[r]])
            # Check if we need to shrink the window
            if (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            # Update the max_len with the size of the current valid window
            max_len = max(max_len, r - l + 1)
        return max_len