n, m = map(int, input().split())
b = list(map(int, input().split()))

left = [x for x in b if x > 0]
right = [-x for x in b if x < 0]

left.sort()
right.sort()

total = 0
for i in range(len(left)-1, -1, -m):
    total += left[i] * 2

for j in range(len(right)-1, -1, -m):
    total += right[j] * 2

max_dist = max(left[-1] if left else 0,
              right[-1] if right else 0)

total -= max_dist

print(total)