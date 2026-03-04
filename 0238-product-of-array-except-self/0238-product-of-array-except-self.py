class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1

        prefix_product = [1]
        suffix_product = [1]

        for num in nums:
            prefix *= num
            prefix_product.append(prefix)

        nums = nums[::-1]
        suffix = 1
        for i in range(len(nums)):
            suffix *= nums[i]
            suffix_product.append(suffix)

        prefix_product.append(1)
        suffix_product.append(1)
        suffix_product.reverse()


        result = []
        j = 1
        for i in range(len(nums)):
    
            result.append(prefix_product[j-1]*suffix_product[j+1])
            j += 1
        
        return result
