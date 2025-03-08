import sys
input = sys.stdin.readline


n, k = map(int, input().split())

cnt = 0

coin_list = [int(input()) for _ in range(n)]
coin_list.sort(reverse=True)

for coin in coin_list:

    cnt += k // coin     
    k %= coin

print(cnt)