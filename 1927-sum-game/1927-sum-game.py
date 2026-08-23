class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        diff = 0
        q_left = 0
        q_right = 0

        for i, ch in enumerate(num):
            if ch == '?':
                if i < half:
                    q_left += 1
                else:
                    q_right += 1
            else:
                if i < half:
                    diff += int(ch)
                else:
                    diff -= int(ch)

        # Bob can win only if the fixed difference can exactly
        # be compensated by the '?' characters.
        #
        # Required:
        # diff = 9 * (q_right - q_left) / 2
        #
        # Avoid floating point by multiplying both sides by 2.
        return 2 * diff != 9 * (q_right - q_left)
