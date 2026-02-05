class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        prefix = ""
        strs.sort()
        first , last = strs[0], strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return prefix
            prefix += first[i]
        return prefix




        