t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    ans = float('inf')
    
    for i in range(n):
        
        if i + 1 < n and s[i] == 'a' and s[i+1] == 'a':
            ans = 2
        
        
        if i + 2 < n and s[i] == 'a' and s[i+2] == 'a':
            ans = min(ans, 3)
        
      
        if i + 3 < n and s[i] == 'a' and s[i+3] == 'a':
            if s[i+1] != s[i+2]:
                ans = min(ans, 4)
        
        
        if i + 6 < n:
            if s[i:i+7] == "abbacca" or s[i:i+7] == "accabba":
                ans = min(ans, 7)
    
    print(ans if ans != float('inf') else -1)
