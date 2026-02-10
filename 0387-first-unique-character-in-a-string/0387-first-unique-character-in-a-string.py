class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_s = Counter(s)
        for i in range(len(s)):
            if dict_s[s[i]] == 1:
                return i


        return -1


