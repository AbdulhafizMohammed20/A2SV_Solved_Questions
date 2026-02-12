class Solution:
    def findValidPair(self, s: str) -> str:
        
        freq = Counter(s)

        left , right  = 0,1
        while right < len(s):
            if int(s[left])  != int(s[right]) :
                if freq[s[left]] == int(s[left])   and freq[s[right]] == int(s[right]):
                    return s[left:right+1]
                
            left = right
            right += 1


        return ""
''
