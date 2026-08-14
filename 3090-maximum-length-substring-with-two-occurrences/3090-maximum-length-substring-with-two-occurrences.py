class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        freq = {}
        max_length = 0
        
        for right in range(len(s)):
            # Add the right character to the window
            freq[s[right]] = freq.get(s[right], 0) + 1
            
            # Shrink window if any character exceeds 2 occurrences
            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            
            # Update maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length