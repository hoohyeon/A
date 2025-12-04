n, k = map(int, input().split())
h = list(map(int, input().split()))

gap = [h[i+1] - h[i] for i in range(n-1)]

# 큰 차이 지점 k-1개 제외
print(sum(sorted(gap)[:n-k]))