n = int(input())
s = [tuple(map(int, input().split())) for _ in range(n)]
s.sort()

m = 0
for i in range(n):
    m += (s[i][0] * (i+1) + s[i][1])
    
print(m)