class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_sum = 0
        
        hash_map = defaultdict(int)
        hash_map[0] = 1
        
        result = 0
        for num in nums :

            prefix_sum += num

            if prefix_sum - k in hash_map:
                result += hash_map[prefix_sum - k]
    
            hash_map[prefix_sum] += 1

        return result


            

            

