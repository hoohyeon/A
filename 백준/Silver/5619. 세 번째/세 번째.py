import sys
input = sys.stdin.readline

n = int(input())
x = [int(input()) for _ in range(n)]

x.sort()
x = x[0:4]

result = []
for i in range(len(x)):
    for j in range(len(x)):
        if i != j:
            result.append(int(str(x[i]) + str(x[j])))

result.sort()
print(result[2])