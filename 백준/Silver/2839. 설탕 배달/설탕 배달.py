sugar = int(input())

a = sugar // 5
b = -1
for i in range(a, -1, -1):
    if (sugar - 5 * i) % 3 == 0:
        a = i
        b = (sugar - 5 * i) // 3
        break

if b != -1:
    print(a+b)
else:
    print(-1)