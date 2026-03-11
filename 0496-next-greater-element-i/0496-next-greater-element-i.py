class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        output = []
        for num in nums2:

            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        
        for i in nums1:
            if i in next_greater:
                output.append(next_greater[i])
            else:
                output.append(-1)
        return output


              