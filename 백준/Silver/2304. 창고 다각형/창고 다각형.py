n = int(input())
height = [0] * 1001

for _ in range(n):
    l, h = map(int, input().split())
    height[l] = h
    
max_h = max(height)
max_idx = height.index(max_h)

area = 0

# 왼쪽부터 탐색
current = 0
for i in range(max_idx+1):
    current = max(current, height[i])
    area += current

# 오른쪽부터 탐색
current = 0
for i in range(1000, max_idx, -1):
    current = max(current, height[i])
    area += current
    
print(area)