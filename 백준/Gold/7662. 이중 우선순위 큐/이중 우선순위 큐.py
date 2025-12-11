import sys, heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())

    max_heap, min_heap = [], []
    visit = [False] * k
    
    for i in range(k):
        m, n = input().split()
        n = int(n)

        # I
        if m == 'I':
            heapq.heappush(max_heap, (-n, i))
            heapq.heappush(min_heap, (n, i))
            visit[i] = True

        # D
        else:
            # max
            if n == 1:
                while max_heap and not visit[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)                 

            # min
            else:
                while min_heap and not visit[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visit[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
    
    # invalid node
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)

    # print
    if not max_heap or not min_heap:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])