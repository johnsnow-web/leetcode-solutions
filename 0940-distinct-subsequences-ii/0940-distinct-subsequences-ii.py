class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        # dp = number of distinct subsequences including empty string
        dp = 1

        # last[c] = dp value before the previous occurrence of c
        last = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')

            new_dp = (2 * dp - last[i]) % MOD

            last[i] = dp
            dp = new_dp

        # Remove the empty subsequence
        return (dp - 1) % MOD
