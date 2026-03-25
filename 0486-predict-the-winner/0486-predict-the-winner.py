class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        def check(p1, p2, l , r, turn):
            if(l > r):
                return [p1, p2]
            left, right = True, False
            if(turn):
                a, b = check(p1+nums[l], p2, l+1 , r, not turn)
                c, d = check(p1+nums[r], p2 ,l , r-1, not turn)
                if(a > c):
                    return [a, b]
                else:
                    return c, d
            else:
                a, b = check(p1, p2+nums[l], l+1 , r, not turn)
                c, d = check(p1, p2+nums[r] ,l , r-1, not turn)
                if(b > d):
                    return a, b
                else:
                    return c, d

        a, b = check(0, 0, 0, n, True)
        return a >= b


