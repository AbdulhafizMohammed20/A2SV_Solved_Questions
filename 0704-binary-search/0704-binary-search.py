class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
       

        def find_indx(low ,high, arr) :

            while low <= high:

                mid = (low + high) // 2

                if target == arr[mid] :
                    return mid
                elif target > arr[mid] :
                    low = mid + 1
                    
                else:
                    high = mid - 1
                
            
            return -1
        
        return find_indx(low, high , nums)
        
            


