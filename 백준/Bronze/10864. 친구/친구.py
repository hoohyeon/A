n, m = map(int, input().split())

students = [0] * n

for _ in range(m):
    a, b = map(int, input().split())

    students[a-1] += 1
    students[b-1] += 1

for student in students:
    print(student)