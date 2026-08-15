class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Calculate XOR of all elements
        total_xor = 0
        for num in nums:
            total_xor ^= num
        
        # If XOR of all elements is non-zero, take all
        if total_xor != 0:
            return n
        
        # If XOR is 0, check if there's any non-zero element to exclude
        for num in nums:
            if num != 0:
                return n - 1
        
        # All elements are 0
        return 0