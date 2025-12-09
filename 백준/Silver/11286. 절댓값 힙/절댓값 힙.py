import sys, heapq
input = sys.stdin.readline

n = int(input())
h = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if h:
            abs_h, sign = heapq.heappop(h)
            print(abs_h * sign)
        else:
            print(0)

    else:
        if x > 0:
            heapq.heappush(h, (x, 1))

        else:
            heapq.heappush(h, (-x, -1))