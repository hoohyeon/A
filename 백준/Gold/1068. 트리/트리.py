n = int(input())
tree = list(map(int, input().split()))
d = int(input())

def dfs(x):
    tree[x] = -2

    for i in range(n):
        if tree[i] == x:
            dfs(i)

dfs(d)

cnt = 0
for i in range(len(tree)):
    if tree[i] != -2 and i not in tree:
        cnt += 1

print(cnt)