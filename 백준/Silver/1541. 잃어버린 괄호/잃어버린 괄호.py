n = input()
m = n.split('-')

ans = sum(map(int, m[0].split('+')))

for number in m[1:]:
    ans -= (sum(map(int, number.split('+'))))

print(ans)