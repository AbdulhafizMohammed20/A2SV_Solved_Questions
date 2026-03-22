class Solution:
    def lastRemaining(self, n: int) -> int:
        
        first_num = 1

        step = 1

        left = True

        while n > 1:

            if left or n %2 == 1:
                first_num += step
            
            n //= 2
            step *= 2
            left = not left
        
        return first_num