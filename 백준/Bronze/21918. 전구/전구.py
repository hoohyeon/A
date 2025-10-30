n, m = map(int, input().split())

bulbs = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())

    if a == 1:
        bulbs[b-1] = c
    
    elif a == 2:
        for i in range(b-1, c):
            if bulbs[i] == 0:
                bulbs[i] = 1
            elif bulbs[i] == 1:
                bulbs[i] = 0

    elif a == 3:
        for i in range(b-1, c):
            bulbs[i] = 0

    elif a == 4:
        for i in range(b-1, c):
            bulbs[i] = 1

print(*bulbs)