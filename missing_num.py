class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_num = 0
        total = (len(nums) *(len(nums) + 1))//2
        total_nums = sum(nums)
        return total - total_nums
        
