# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # for i in range(1, n +1 ):

        #     if isBadVersion(i):
        #         return i

        left = 0
        right = n
        ans = 0

        while left <= right :

            mid = (left + right ) // 2

            if isBadVersion(mid): 
                ans = mid
                right = mid - 1

            else:
                left = mid + 1
            
        return ans
        
                
        
                

            
