class Solution:
    def frequencySort(self, s: str) -> str:

        freq = Counter(s)
        # print(freq)
        list_s = []
        for key , val in freq.items():
            list_s.append([val,key])
        
        list_s.sort()
        list_s = list_s[::-1]
        # print(list_s)

        s1 = ''

        for i in range(len(list_s)):
            val , char = list_s[i]

            while val:
                s1 += char
                val -= 1
            
        return s1

        