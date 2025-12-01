n = int(input())
s = [int(input()) for _ in range(n)]

m = max(s)
freq = [0] * (m+1)
hit = [-1] * (m+1)

for x in s:
    freq[x] += 1

for i in range(m+1):
    if freq[i] == 0:
        continue
    
    for j in range(i, m+1, i):
        hit[j] += freq[i]

for i in range(n):
    k = s[i]
    print(hit[k])