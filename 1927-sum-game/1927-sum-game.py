class Solution:
    def sumGame(self, num: str) -> bool:
        half = len(num) // 2

        diff = 0
        q_diff = 0

        for i, ch in enumerate(num):
            if ch == '?':
                q_diff += 1 if i < half else -1
            else:
                diff += int(ch) if i < half else -int(ch)

        return 2 * diff + 9 * q_diff != 0
