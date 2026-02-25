class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        arr = [0] * len(nums)

        for i in range(len(nums)):
            arr[i] = nums[i]

        arr.sort()

        dictionary = defaultdict(int)
        for i in range(len(arr)):
            if arr[i] not in dictionary:
                dictionary[arr[i]] += i

        result = []

        for num in nums:
            result.append(dictionary[num])

        return result
