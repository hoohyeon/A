N = int(input())
M = int(input())
x = list(map(int, input().split()))

# 1. 처음
answer = x[0]

# 2. 중간
for i in range(M-1):
    gap = x[i+1] - x[i]
    answer = max(answer, (gap + 1) // 2)
    
# 3. 끝
answer = max(answer, N - x[-1])

print(answer)