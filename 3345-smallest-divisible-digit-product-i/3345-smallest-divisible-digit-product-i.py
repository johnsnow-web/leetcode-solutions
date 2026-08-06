class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            # Calculate product of digits
            product = 1
            temp = n
            while temp > 0:
                product *= temp % 10
                temp //= 10
            
            # Check if divisible by t
            if product % t == 0:
                return n
            
            n += 1