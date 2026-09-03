class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')

        # Find the smallest odd number
        for x in nums1:
            if x & 1:
                min_odd = min(min_odd, x)

        # No odd numbers -> all are already even
        if min_odd == float('inf'):
            return True

        # Every even number must be >= min_odd
        for x in nums1:
            if (x & 1) == 0 and x < min_odd:
                return False

        return True
