class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # handle k > n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: reverse whole array
        reverse(0, n-1)
        # Step 2: reverse first k
        reverse(0, k-1)
        # Step 3: reverse rest
        reverse(k, n-1)