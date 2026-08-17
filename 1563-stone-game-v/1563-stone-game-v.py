from functools import cache
from itertools import accumulate


class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        if n <= 1:
            return 0

        # Prefix sums
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(l, r):
            if l >= r:
                return 0

            ans = 0
            left = 0
            right = prefix[r + 1] - prefix[l]

            for k in range(l, r):
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    # Alice keeps left.
                    #
                    # If ans >= 2 * left, then even the best possible
                    # result from this split cannot beat ans.
                    if ans >= left * 2:
                        continue

                    ans = max(ans, left + dfs(l, k))

                elif left > right:
                    # Alice keeps right.
                    #
                    # Since right will only decrease afterwards,
                    # if ans >= 2 * right, no later split can improve it.
                    if ans >= right * 2:
                        break

                    ans = max(ans, right + dfs(k + 1, r))

                else:
                    # Equal sums: Alice can choose either side.
                    ans = max(
                        ans,
                        left + dfs(l, k),
                        right + dfs(k + 1, r)
                    )

            return ans

        return dfs(0, n - 1)