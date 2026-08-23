class Solution:
    def sumGame(self, num: str) -> bool:
        middle = len(num) // 2
        left_part = num[:middle]
        right_part = num[middle:]

        left_sum = sum(
            int(char) for char in left_part if char != "?"
        )
        right_sum = sum(
            int(char) for char in right_part if char != "?"
        )

        left_questions = left_part.count("?")
        right_questions = right_part.count("?")

        if (left_questions + right_questions) % 2 != 0:
            return True

        sum_diff = left_sum - right_sum
        question_diff = right_questions - left_questions

        return sum_diff * 2 != question_diff * 9