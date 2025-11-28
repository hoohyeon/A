n = int(input())
dec = []

def bt(num):
    dec.append(int(num))

    for i in range(10):
        if i < int(num[-1]):
            new = num + str(i)
            bt(new)
        else:
            break

for i in range(10):
    bt(str(i))

if n >= len(dec):
    print(-1)
else:
    print(sorted(dec)[n])