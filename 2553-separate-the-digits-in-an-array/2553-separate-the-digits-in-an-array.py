class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result =  []

        for num in nums:
            if num > 9 :
                digits = []
                while num :
                    digits.append(num% 10)
                    num = num // 10

                digits = digits[::-1]
                result.extend(digits)
                    
            else:
                result.append(num)
            
        return result