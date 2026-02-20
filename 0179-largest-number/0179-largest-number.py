class Solution:
    def largestNumber(self, nums: List[int]) -> str:
   
        str_nums = [str(x) for x in nums]
        # result = ''
        n = len(str_nums)

        for i in range(n):
            for j in range(n-i-1):
                
                if str_nums[j] + str_nums[j+1] < str_nums[j+1] + str_nums[j]:
                    str_nums[j], str_nums[j+1] = str_nums[j+1], str_nums[j]
                
        result = ''.join(str_nums)
        return '0' if result[0] == '0' else result

        # print(result)



            
        
