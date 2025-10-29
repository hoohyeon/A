n = input()
l = len(n)

left_sum, right_sum = 0, 0

for i in range(l//2):
    left_sum += int(n[i])

for j in range(l//2, l):
    right_sum += int(n[j])

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')