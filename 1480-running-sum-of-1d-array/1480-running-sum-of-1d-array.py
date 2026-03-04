class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        running_sum = []
        prefix = 0

        for num in nums:
            prefix += num
            running_sum.append(prefix)
        
        return running_sum 

