n = int(input())

plan = [(tuple(map(int, input().split()))) for _ in range(n)]

plan.sort(key=lambda x:x[1], reverse=True)

current = plan[0][1] + 1

for p in plan:
    t, s = p

    if current > s:
        current = s

    current -= t

print(current if current >= 0 else -1)