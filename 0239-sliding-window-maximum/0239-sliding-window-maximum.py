class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque()
        n = len(nums)
        result = []
        for right in range(n):
            if queue and right - queue[0] + 1 > k:
                queue.popleft()
            while queue and nums[queue[-1]] <= nums[right]:
                queue.pop()
            queue.append(right)
            if(right+1 >= k):
                result.append(nums[queue[0]])
        return result

