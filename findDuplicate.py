class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        nums.sort()

        l , r = 0 , 1
        result = []
        while r < len(nums):
            if nums[l] == nums[r]:
                result.append(nums[l])
                l += 1
                r += 1
            l += 1
            r+= 1
        return result
            


            




