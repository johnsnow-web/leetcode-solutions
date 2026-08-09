class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        # Compute suffix sums for O(1) range queries
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        
        # Memoization cache
        memo = {}
        
        def dp(index, m):
            # Base case: no more piles
            if index >= n:
                return 0
            
            # Check memoization
            if (index, m) in memo:
                return memo[(index, m)]
            
            # Try taking X piles where 1 <= X <= min(2*m, remaining piles)
            max_stones = 0
            for x in range(1, min(2 * m, n - index) + 1):
                # Stones from first X piles + (what's left) - (what opponent gets)
                current = suffix[index] - dp(index + x, max(m, x))
                max_stones = max(max_stones, current)
            
            memo[(index, m)] = max_stones
            return max_stones
        
        return dp(0, 1)