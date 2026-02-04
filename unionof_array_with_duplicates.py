class Solution:    
    def findUnion(self, a, b):
        # code here
        a.extend(b)
        a.sort()
        result = [a[0]]
        for i in range(1,len(a)):
            if a[i] != result[-1]:
                result.append(a[i])
            
            
        return result
                
            
        
        
