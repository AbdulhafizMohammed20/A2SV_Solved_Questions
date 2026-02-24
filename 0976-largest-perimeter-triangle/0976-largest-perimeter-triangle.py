class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()

        perimeter = 0

        for i in range(2,len(nums)):
            if (nums[i-1] + nums[i - 2] ) > nums[i] :

                perimeter = max(perimeter , (nums[i-1] + nums[i - 2] ) + nums[i])
            
        return perimeter

                


