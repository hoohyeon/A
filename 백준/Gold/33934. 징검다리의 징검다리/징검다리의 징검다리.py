n, s, e = map(int, input().split())
A = list(map(int, input().split()))
k = int(input())

min_k = abs(s - e) + 1

l = min(s, e) - 1
r = max(s, e) - 1

while l - 1 >= 0:
    if A[l] == 1:
        break
    l -= 1

while r + 1 < n:
    if A[r] == 1:
        break
    r += 1

max_k = sum(A[l:r+1])

print(1 if min_k <= k <= max_k else 0)