class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Step 1: Find longest sequential prefix and its sum
        seq_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Check if nums[i] = nums[i-1] + 1
            if nums[i] == nums[i - 1] + 1:
                seq_sum += nums[i]
            else:
                break
        
        # Step 2: Convert array to set for O(1) lookup
        num_set = set(nums)
        
        # Step 3: Find smallest integer >= seq_sum not in the array
        x = seq_sum
        while x in num_set:
            x += 1
        
        return x