class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]

        for num in nums :
            new_set = [curr + [num] for curr in res]
            res.extend(new_set)
        
        return res