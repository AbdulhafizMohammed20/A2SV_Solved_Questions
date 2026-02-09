class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict_nums = Counter(nums)
        result = []

        for key, val in dict_nums.items():
            result.append([val,key])

        result.sort()

        result = result[::-1]

        ans = []

        for list_num in result :
            if len(ans) < k:
                ans.append(list_num[-1])  
        
        return ans