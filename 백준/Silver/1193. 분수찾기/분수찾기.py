x = int(input())

cnt, n = 0, 0

while cnt < x:
    n += 1
    cnt += n

offset = x - (cnt - n)

a, b = str(offset), str(n - offset + 1)

if n % 2 == 1:
    print(b+'/'+a)

else:
    print(a+'/'+b)