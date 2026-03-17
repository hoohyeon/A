import sys
input = sys.stdin.readline

n = int(input())
rank = [int(input()) for _ in range(n)]
rank.sort()

gap = 0
for i in range(n):
    gap += abs((i+1) - rank[i])
    
print(gap)