import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    c = input().split()

    if len(c) > 1:
        x = int(c[1])

    if c[0] == 'add':
        s.add(x)
    elif c[0] == 'remove':
        if x in s:
            s.remove(x)
    elif c[0] == 'check':
        if x in s:
            print(1)
        else:
            print(0)
    elif c[0] == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)   
    elif c[0] == 'all':
        s = {i for i in range(1, 21)}
    elif c[0] == 'empty':
        s = set()