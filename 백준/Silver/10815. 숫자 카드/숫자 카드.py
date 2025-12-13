n = int(input())
cards = list(map(int, input().split()))

m = int(input())
other = list(map(int, input().split()))

dic = {}

for c in cards:
    dic[c] = 0

for o in other:
    if o in dic:
        print(1, end=' ')
    else:
        print(0, end=' ')