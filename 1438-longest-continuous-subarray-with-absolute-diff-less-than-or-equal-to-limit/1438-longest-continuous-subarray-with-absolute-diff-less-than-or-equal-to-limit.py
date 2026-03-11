class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        maxDeque = deque()
        minDeque = deque()
        left = 0
        result = 0

        for i in range (len(nums)):

            while maxDeque and nums[i] > maxDeque[-1] :
                maxDeque.pop()


            while minDeque and nums[i] < minDeque[-1] :
                minDeque.pop()

            maxDeque.append(nums[i])
            minDeque.append(nums[i])

            while maxDeque and minDeque and  maxDeque[0] - minDeque[0] > limit :

                if nums[left] == maxDeque[0]  :
                    maxDeque.popleft()
                
                if nums[left] == minDeque[0] :
                    minDeque.popleft()
                
                left += 1
            
            result = max(result, i - left + 1)

        return result

            



