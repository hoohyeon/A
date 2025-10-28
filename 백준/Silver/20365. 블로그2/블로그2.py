n = int(input())

s = input()

blue, red = 0, 0

if s[0] == 'B':
    blue += 1
else:
    red += 1
    
for i in range(1, n):
    if s[i] != s[i-1]:
        if s[i] == 'B':
            blue += 1
        else:
            red += 1
            
print(min(blue, red) + 1)