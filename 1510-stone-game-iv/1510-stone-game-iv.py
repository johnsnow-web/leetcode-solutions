
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] = True if current player wins with i stones
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            # Try removing all perfect squares <= i
            j = 1
            while j * j <= i:
                # If opponent loses after our move, we win
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1
        
        return dp[n]