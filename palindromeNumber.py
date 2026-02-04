class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check if it is negative since negative integers aren't palindrome
        if x < 0:
            return False
        # convert its data types to strings to make it easy to slice and iterate over it
        changed_tostr = str(x)
        #Initialize two pointers to track and compare from both sides of the digit
        left, right = 0,len(changed_tostr) -1
        while left <= right:

            if changed_tostr[left] != changed_tostr[right]:
                return False
            left += 1
            right -= 1

        return True

        
