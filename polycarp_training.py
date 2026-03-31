n = int(input())

a = list(map(int, input().split()))

a.sort()

day = 1


for contest_size in a:

    if contest_size >= day:
     
        day = day + 1


print(day - 1)
