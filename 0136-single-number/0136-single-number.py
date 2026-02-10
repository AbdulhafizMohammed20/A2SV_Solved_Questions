class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dict_nums = Counter(nums)

        for key,val in dict_nums.items():
            if val == 1:
                return key