class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(set(nums))
        buckets = []
        for i in range(n) :
            buckets.append([])

        ans = []
        hash_map = Counter(nums)

        for key, val in hash_map.items():
            buckets.append([val,key])
        
        buckets.sort()
        buckets = buckets[::-1]

        for i in range(k):
            ans.append(buckets[i][1])

        return ans


       
