class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left = 0
        right = int(sqrt(c)) + 1
        while left <= right :
            if pow(left, 2) + pow(right, 2) == c:
                return True
            elif pow(left, 2) + pow(right, 2) > c:
                right -= 1
            else:
                left += 1
        return False
            

