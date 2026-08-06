class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(num):
            prod = 1
            while num > 0:
                prod *= num % 10
                num //= 10
            return prod
        
        # Convert n to digit array
        s = str(n)
        digits = [int(d) for d in s]
        length = len(digits)
        
        # Check if n itself works
        if digit_product(n) % t == 0:
            return n
        
        # Try modifying each position from right to left
        # Key optimization: when incrementing a digit at position i,
        # set all digits after it to 0 (gives smallest possible number)
        for pos in range(length - 1, -1, -1):
            # Try each digit value greater than current
            for digit in range(digits[pos] + 1, 10):
                # Form candidate: keep prefix, set pos to digit, fill rest with 0s
                candidate = int(''.join(map(str, digits[:pos])) + str(digit) + '0' * (length - pos - 1))
                if digit_product(candidate) % t == 0:
                    return candidate
        
        # If no solution found in same length, answer is 10...0 (1 followed by length zeros)
        # Its product is always 0, divisible by any t
        return 10 ** length