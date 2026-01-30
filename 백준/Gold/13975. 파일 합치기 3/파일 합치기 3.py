import heapq

t = int(input())

for _ in range(t):
    k = int(input())
    f = list(map(int, input().split()))

    heapq.heapify(f)

    cost = 0
    
    while len(f) > 1:
        a = heapq.heappop(f)
        b = heapq.heappop(f)

        c = a + b
        
        cost += c
        heapq.heappush(f, c)

    print(cost)