a, b = map(int, input().split())
n = int(input())
freq = [int(input()) for _ in range(n)]

min_gap = abs(b-a)
for f in freq:
    min_gap = min(min_gap, abs(f - b) + 1)
    
print(min_gap)