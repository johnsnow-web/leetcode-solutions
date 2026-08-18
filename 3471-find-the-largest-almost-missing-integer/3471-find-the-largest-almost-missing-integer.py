class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Get all unique values
        unique_vals = set(nums)
        
        # For each value, count how many subarrays of size k contain it
        subarray_count = {}
        
        for val in unique_vals:
            count = 0
            # Check each subarray of size k
            for i in range(n - k + 1):
                # Check if val appears in subarray [i, i+k)
                if val in nums[i:i+k]:
                    count += 1
            subarray_count[val] = count
        
        # Find all values appearing in exactly 1 subarray
        almost_missing = [val for val, count in subarray_count.items() if count == 1]
        
        # Return the largest, or -1 if none exist
        return max(almost_missing) if almost_missing else -1