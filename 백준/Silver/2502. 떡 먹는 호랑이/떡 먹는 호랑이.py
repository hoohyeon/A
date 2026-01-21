d, k = map(int, input().split())

dp_A = [0] * (d+1)
dp_B = [0] * (d+1)

for i in range(1, d+1):
    if i == 1:
        dp_A[i] = 1
        dp_B[i] = 0

    elif i == 2:
        dp_A[i] = 0
        dp_B[i] = 1

    else:
        dp_A[i] = dp_A[i-1] + dp_A[i-2]
        dp_B[i] = dp_B[i-1] + dp_B[i-2]

a, b = dp_A[d], dp_B[d]

# 만족하는 가장 작은 A 찾기
for i in range(1, k//a + 1):
    if (k - (a * i)) % b == 0:
        A = i
        B = (k - (a * i)) // b
        break
        
print(A)
print(B)