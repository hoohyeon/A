n = input()

li = list(map(int, n))

li.sort(reverse=True)

for l in li:
    print(l, end='')