class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        result = []

        dict_nums = Counter(nums)

        for key , val in dict_nums.items():

            if val > len(nums)//3:
                result.append(key)
        return result