class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = min((x for x in nums1 if x & 1), default=None)

        return (
            min_odd is None
            or all(x >= min_odd for x in nums1 if x % 2 == 0)
        )
