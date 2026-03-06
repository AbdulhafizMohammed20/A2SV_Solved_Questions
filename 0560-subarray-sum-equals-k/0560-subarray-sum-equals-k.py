class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix =[0]
        prev = 0

        for num in nums : 
            prev += num 
            prefix.append(prev)
        
        hash_map = defaultdict(int)
        
        result = 0
        # pre + x = k
        for pre in prefix :

            if pre - k in hash_map:
                result += hash_map[pre - k]
    
            hash_map[pre] += 1

        return result


            

            

