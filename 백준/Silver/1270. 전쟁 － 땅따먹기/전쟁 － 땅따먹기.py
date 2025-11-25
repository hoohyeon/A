from collections import Counter

n = int(input())

for _ in range(n):
    land = list(map(int, input().split()))

    c = land[0] 
    s = land[1:]

    count = Counter(s)

    count2 = sorted(count.items(), key= lambda x: (-x[1], x[0]))

    if count2[0][1] > (c / 2):
        print(count2[0][0])

    else:
        print('SYJKGW')