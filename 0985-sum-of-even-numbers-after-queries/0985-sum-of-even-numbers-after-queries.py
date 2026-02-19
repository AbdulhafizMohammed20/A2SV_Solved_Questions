class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        initialEvenSum = 0
        evens = []
        for num in nums:
            if num % 2 == 0:
                initialEvenSum += num
        
        for q in queries:
            val, indx = q
            if nums[indx] %2 == 0:
                initialEvenSum -= nums[indx]

            nums[indx] += val
            if nums[indx] %2 == 0:
                initialEvenSum += nums[indx]
            evens.append(initialEvenSum)
            
        return evens

                

