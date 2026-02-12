class Solution:
    def minimumIndex(self, nums: List[int]) -> int:


        # def checkValidSplit(arr,dominantElement):
        #     dict_arr = Counter(arr)
        #     if dict_arr[dominantElement] > (len(arr)//2):
        #         return True
        #     return False

            
        
        # dict_nums = Counter(nums)
        # dominantElement = 0
        # frequency = float("-inf")

        # for key , val in dict_nums.items():
        #     if val > frequency :
        #         frequency = max(frequency, val)
        #         dominantElement = key
            
        
        # Write Your logic Here 👇

        # i =  0
        # while i < len(nums):
        #     if nums[i] == dominantElement:
        #         a = checkValidSplit(nums[:i+1],dominantElement)
        #         b = checkValidSplit(nums[i+1:],dominantElement)
        #         if a and b:
        #             return i
        #         else:
        #             i += 1
        #     else:
        #         i += 1

        freq = Counter(nums)
        dominant = max(freq, key = freq.get)

        totalCount = freq[dominant]
        n =len(nums)
        countLeft = 0

        for i in range(n-1):

            if nums[i] == dominant :
                countLeft += 1
            
            if countLeft > (i+1)//2 and (totalCount - countLeft) > (n-i-1)//2:
                return i
                
        
        return -1

        



