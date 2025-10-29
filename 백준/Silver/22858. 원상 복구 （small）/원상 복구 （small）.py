n, k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))

cur_list = s

for _ in range(k):
    prev_list = [0] * n
    
    for i in range(n):
        prev_list[d[i]-1] = cur_list[i]

    cur_list = prev_list

print(*cur_list)