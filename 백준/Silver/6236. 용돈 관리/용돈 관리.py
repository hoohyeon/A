import sys
input = sys.stdin.readline

n, m = map(int, input().split())
prices = [int(input()) for _ in range(n)]

# x원 인출하면 인출하는 횟수
def f(x):
    cnt = 1
    account = x
    for price in prices:
        if account >= price:
            account -= price
        else:
            cnt += 1
            account = x - price

    return cnt

# 최대 인출 횟수를 위한 최소 인출 가격
# 최소 인출 횟수를 위한 최대 인출 가격
left, right = max(prices), sum(prices)

while left <= right:
    mid = (left + right) // 2

    if f(mid) <= m:
        right = mid - 1

    else:
        left = mid + 1

print(left)