class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return False if len(set(nums)) == len(nums) else True

        present = False
        dict_nums = Counter(nums)

        for val in dict_nums.values():

            if val >= 2:
                present = True

        return present