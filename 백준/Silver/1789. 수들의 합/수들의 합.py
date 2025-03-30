s = int(input())

i = 0
sum = 0
while True:
    i += 1
    sum += i

    if sum > s:
        break

print(i-1)