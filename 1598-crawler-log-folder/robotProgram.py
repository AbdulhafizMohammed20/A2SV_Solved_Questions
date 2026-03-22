t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
 
    pref = [0] * (n + 1)
    for i in range(n):
        if s[i] == 'L':
            pref[i + 1] = pref[i] - 1
        else:
            pref[i + 1] = pref[i] + 1
 
    first_hit = -1
    for i in range(1, n + 1):
        if x + pref[i] == 0:
            first_hit = i
            break
 
    if first_hit == -1 or first_hit > k:
        print(0)
        continue
 
 
    cycle_len = -1
    for i in range(1, n + 1):
        if pref[i] == 0:
            cycle_len = i
            break
 
    ans = 1  
 
    if cycle_len != -1:
        ans += (k - first_hit) // cycle_len
 
    print(ans)
