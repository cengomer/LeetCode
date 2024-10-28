class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Dictionary to store the frequency of characters in t
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        # Variables for sliding window
        window_count = {}
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float("inf")
        l = 0
        
        # Move the right pointer to expand the window
        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1
            
            # Check if this character satisfies the frequency requirement from t
            if char in t_count and window_count[char] == t_count[char]:
                have += 1
            
            # Shrink the window from the left when we have all required characters
            while have == need:
                # Update result if this window is smaller than the previous one
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                # Pop the left character from the window
                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
