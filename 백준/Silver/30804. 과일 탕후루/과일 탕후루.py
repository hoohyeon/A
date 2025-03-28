n = int(input())
f = list(map(int, input().split()))

left = 0
max_len = 0
count = {}

for right in range(n):
    if f[right] not in count:
        count[f[right]] = 0
    count[f[right]] += 1

    while len(count) > 2:
        count[f[left]] -= 1
        if count[f[left]] == 0:
            del count[f[left]]
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)