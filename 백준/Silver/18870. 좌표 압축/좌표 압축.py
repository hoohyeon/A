import sys
input = sys.stdin.readline

n = int(input())
X = list(map(int, input().split()))
X2 = sorted(set(X))
ans = {}

for i in range(len(X2)):
    ans[X2[i]] = i

for x in X:
    print(ans[x], end=' ')