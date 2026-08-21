class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)

        # Remove redundant denominations:
        # if a coin is a multiple of another coin, its multiples
        # are already covered by the smaller coin.
        coins.sort()
        useful = []

        for c in coins:
            if not any(c % x == 0 for x in useful):
                useful.append(c)

        coins = useful
        n = len(coins)

        # Precompute LCM for every subset.
        # subset_lcm[mask] = LCM of coins in mask.
        subset_lcm = [1] * (1 << n)
        subset_bits = [0] * (1 << n)

        for mask in range(1, 1 << n):
            bit = mask & -mask
            i = bit.bit_length() - 1
            prev = mask ^ bit

            a = subset_lcm[prev]
            b = coins[i]

            # lcm(a, b)
            l = a // gcd(a, b) * b

            # Values larger than the possible answer can be capped.
            # k is the maximum number of distinct amounts we need.
            if l > k * min(coins):
                l = k * min(coins) + 1

            subset_lcm[mask] = l
            subset_bits[mask] = subset_bits[prev] + 1

        def count(x: int) -> int:
            """Number of distinct positive amounts <= x."""
            total = 0

            for mask in range(1, 1 << n):
                l = subset_lcm[mask]

                if l > x:
                    continue

                cnt = x // l

                if subset_bits[mask] & 1:
                    total += cnt
                else:
                    total -= cnt

            return total

        # The kth amount is at most k * smallest denomination.
        lo = 1
        hi = k * coins[0]

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo
