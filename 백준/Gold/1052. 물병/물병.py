n, k = map(int, input().split())

ones = n.bit_count()

cnt = 0

while ones > k:
    lsb = n & -n
    n += lsb
    cnt += lsb
    ones = n.bit_count()

print(cnt)