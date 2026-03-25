class Solution:
    def isPalindrome(self, x: int) -> bool:
        stri = str(x)
        n = len(stri)
        def check(stri,l ,r) :

            if l >= r :
                return True
            if stri[l] == '-' or stri[l] != stri[r] :
                return False
            
            return check(stri, l +1 , r- 1)
        
        return check(stri, 0 , n-1)