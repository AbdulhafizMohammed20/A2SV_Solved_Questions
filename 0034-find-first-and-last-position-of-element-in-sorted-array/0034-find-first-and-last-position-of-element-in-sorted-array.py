class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if target not in nums :
            return [-1,-1]
        
        left = 0
        right = (len(nums)) - 1
        res = []

        while left <= right :
            mid =  (left + right) //2
            if target == nums[mid] :
                end = mid
                start = mid

                while start > -1 and nums[start] == target :
                    start -= 1
                while end < right + 1 and nums[end] == target :
                    end += 1
                
                return [start+1 , end-1]

            elif target > nums[mid] :

                left = mid + 1
            else:
                right = mid - 1




