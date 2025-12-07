n, l = map(int, input().split())
holes = list(map(int, input().split()))

holes.sort()

cnt = 1
end = holes[0] + l -1

for h in holes:
    if h > end:
        cnt += 1
        end = h + l - 1
        
print(cnt)