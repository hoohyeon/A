n, s = map(int, input().split())
x = list(map(int, input().split()))

start, end = 0, 0
partial_sum = 0
min_len = n+1

while True:
    if partial_sum >= s:
        min_len = min(min_len, end - start)
        partial_sum -= x[start]
        start += 1

    else:
        if end == n:
            break

        partial_sum += x[end]
        end += 1
        
print(0 if min_len == n+1 else min_len)