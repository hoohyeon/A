s = input()
n = len(s)

cnt = 0
for i in range(n-1):
    if s[i] != s[i+1]:
        cnt += 1

print((cnt+1) // 2)