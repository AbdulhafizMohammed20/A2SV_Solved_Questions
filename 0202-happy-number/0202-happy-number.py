class Solution:
    def happy_num(self, n):
        is_happy_num = 0
        while n:
            is_happy_num += pow(n%10,2)
            n //= 10
        return is_happy_num
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.happy_num(n)
        return True if n == 1 else False