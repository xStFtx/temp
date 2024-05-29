class Solution:
    def numSteps(self, s: str) -> int:
        # Convert the binary string to an integer
        num = int(s, 2)
        steps = 0
        
        # Perform operations until the number is reduced to 1
        while num != 1:
            if num % 2 == 0:
                # If the number is even, divide by 2
                num //= 2
            else:
                # If the number is odd, add 1
                num += 1
            steps += 1
        
        return steps