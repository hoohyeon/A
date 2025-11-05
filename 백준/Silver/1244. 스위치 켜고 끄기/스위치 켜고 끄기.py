n = int(input())

bulbs = list(map(int, input().split()))

s = int(input())

for _ in range(s):
    se, num = map(int, input().split())

    idx = num - 1
    if se == 1:
        for i in range(num, n+1, num):
            bulbs[i-1] ^= 1

    else:
        bulbs[idx] ^= 1

        k = 1

        while idx - k >= 0 and idx + k < n and bulbs[idx-k] == bulbs[idx+k]:
            k += 1

        for i in range(1, k):
            bulbs[idx - i] ^= 1
            bulbs[idx + i] ^= 1

for start in range(0, n, 20):
    line = bulbs[start:start + 20]
    print(" ".join(map(str, line)))