sieve = [0] * 2 + [1] * 123456 * 2

# 에라토스테네스의 체
for i in range(2, 123456 * 2 + 1):
    if sieve[i]:
        for j in range(i * 2, 123456 * 2 + 1, i):
            sieve[j] = 0

while True:
    n = int(input())

    if n == 0:
        break
    
    print(sum(sieve[n+1:2*n+1]))