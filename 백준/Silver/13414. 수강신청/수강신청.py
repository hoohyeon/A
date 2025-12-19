import sys
input = sys.stdin.readline

K, L = map(int, input().split())

order = {}

for _ in range(L):
    student = input().strip()
    order.pop(student, None)
    order[student] = None

for i, student in enumerate(order):
    if i == K:
        break
    print(student)