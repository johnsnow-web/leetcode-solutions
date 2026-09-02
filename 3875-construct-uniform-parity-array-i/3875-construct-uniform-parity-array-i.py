class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # One element cannot be changed using another index.
        if len(nums1) == 1:
            return True

        # For n >= 2, we can always make all elements have
        # the same parity.
        return True
