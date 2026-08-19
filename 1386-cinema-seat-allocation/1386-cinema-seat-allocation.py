class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Store reserved seats as a bitmask for each affected row.
        rows = {}

        for r, s in reservedSeats:
            rows[r] = rows.get(r, 0) | (1 << s)

        # Masks for:
        # [2,3,4,5], [4,5,6,7], [6,7,8,9]
        LEFT = sum(1 << s for s in range(2, 6))
        MID  = sum(1 << s for s in range(4, 8))
        RIGHT = sum(1 << s for s in range(6, 10))

        # All unaffected rows can accommodate 2 groups.
        ans = 2 * (n - len(rows))

        for mask in rows.values():
            left_free = (mask & LEFT) == 0
            mid_free = (mask & MID) == 0
            right_free = (mask & RIGHT) == 0

            if left_free and right_free:
                # [2-5] and [6-9] don't overlap.
                ans += 2
            elif left_free or mid_free or right_free:
                ans += 1

        return ans