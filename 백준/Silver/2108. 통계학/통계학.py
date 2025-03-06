import sys
input = sys.stdin.readline

n = int(input())
arr = []
freq = {}

for _ in range(n):
    z = int(input())
    arr.append(z)

print(round(sum(arr) / n))

arr.sort()
print(arr[(n-1)//2])

for num in arr:
    freq[num] = freq.get(num, 0) + 1

# 최빈값 찾기
max_count = max(freq.values())
modes = [num for num, count in freq.items() if count == max_count ]
if len(modes) >= 2:
    print(modes[1])
else:
    print(modes[0])

print((arr[-1]-arr[0]))