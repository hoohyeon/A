n = int(input())
b = list(map(int, input().split()))
r = [0] * n

for i in range(n-1):

    temp = -(int(1e9))
    for j in range(i+1, n):

        slope = (b[j] - b[i]) / (j - i)

        if temp < slope:
            r[i] += 1
            r[j] += 1

            temp = slope

print(max(r))