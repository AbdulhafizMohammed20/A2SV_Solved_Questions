class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        
        for i in range(len(responses)):
            responses[i] = list(set(responses[i]))
        
        freq = defaultdict(int)

        for i in range(len(responses)):
            for j in range(len(responses[i])):
                freq[responses[i][j]] += 1

        max_val = max(freq.values())
        most_common = [k for k, v in freq.items() if v == max_val]
        most_common.sort()
        return most_common[0]
        


        



