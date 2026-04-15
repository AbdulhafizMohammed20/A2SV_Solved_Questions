class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        hash_map = Counter(nums) 
        result = []
        nums.sort()
        for key, val in hash_map.items():

            if val > 1:
                result.append(key)
        
        for i in range(1, len(nums)+1):

            if i not in hash_map:
                result.append(i)
            
        # result.sort()

        return result
