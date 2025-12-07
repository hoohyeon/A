n = int(input())
m = int(input())
s = input()

cnt, ans, i = 0, 0, 0
while i < m-1:
    if s[i:i+3] == 'IOI':
        cnt += 1
        i += 2
        
        if cnt == n:
            ans += 1
            cnt -= 1            
    else:
        cnt = 0
        i += 1
        
print(ans)