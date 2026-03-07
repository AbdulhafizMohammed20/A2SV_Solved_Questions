class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = Counter(nums)

        for key in hash_map :

            if hash_map[key] == 1:
                return key