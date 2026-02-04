class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        a.sort()
        b.sort()
        
        flag = True
        for i in range(len(a)):
            if a[i] != b[i]:
                flag = False
                # print(flag)
                return flag
        
        return flag
                
