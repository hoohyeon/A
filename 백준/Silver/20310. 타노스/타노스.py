s = input()

# 0, 1 개수
c0, c1 = s.count('0'), s.count('1')
d0, d1 = c0 // 2, c1 // 2

# 앞에서부터 1 제거
temp = []
for ch in s:
    if ch == '1' and d1 > 0:
        d1 -= 1
    else:
        temp.append(ch)

# 뒤에서부터 0 제거
ans = []
for ch in reversed(temp):
    if ch == '0' and d0 > 0:
        d0 -= 1
    else:
        ans.append(ch)
        
print(''.join(reversed(ans)))