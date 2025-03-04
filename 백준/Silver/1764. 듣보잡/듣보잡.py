import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cantsee = []
canthear = []

for _ in range(n):
    name = input().strip()

    cantsee.append(name)

for _ in range(m):
    name = input().strip()

    canthear.append(name)

cantseeandhear = set(cantsee) & set(canthear)

print(len(cantseeandhear))
for people in sorted(cantseeandhear):
    print(people)
