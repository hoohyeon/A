ISBN = input()

total = 0
t_idx = 0
t_num = 0

for i in range(13):
    if ISBN[i] == '*':
        t_idx = i
        continue

    weight = 1 if i % 2 == 0 else 3
    total += int(ISBN[i]) * weight

weight = 1 if t_idx % 2 == 0 else 3
for i in range(10):
    if (total + i * weight) % 10 == 0:
        t_num = i
        break

print(t_num)