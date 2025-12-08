h, w = map(int, input().split())
height = list(map(int, input().split()))

max_left = [0] * w
max_right = [0] * w

max_left[0] = height[0] 
for i in range(1, w):
    max_left[i] = max(max_left[i-1], height[i])
    
max_right[w-1] = height[w-1]
for i in range(w-2, -1, -1):
    max_right[i] = max(max_right[i+1], height[i])

rain = 0
for i in range(w):
    rain += min(max_left[i], max_right[i]) - height[i]

print(rain)