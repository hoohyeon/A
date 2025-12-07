n, x = map(int, input().split())
visit = list(map(int, input().split()))

window = sum(visit[:x])
max_sum = window
cnt = 1

for i in range(1, n-x+1):
    window += visit[i+x-1] - visit[i-1]

    if window > max_sum:
        max_sum = window
        cnt = 1
        
    elif window == max_sum:
        cnt += 1
        
if max_sum == 0:
    print('SAD')

else:
    print(max_sum)
    print(cnt)