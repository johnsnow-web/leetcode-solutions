class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seq_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                seq_sum += nums[i]
            else:
                break
        
        x = seq_sum
        while any(num == x for num in nums):
            x += 1
        return x