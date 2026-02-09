class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        steps = 0

        dict_s = Counter(s)
        dict_t = Counter(t)

        for key in dict_s:
            if dict_s[key] > dict_t[key]:
                steps += dict_s[key] - dict_t[key]

        return steps