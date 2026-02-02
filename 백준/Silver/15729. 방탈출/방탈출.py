n = int(input())
note = list(map(int, input().split()))

button = [0] * n
cnt = 0

for i in range(n):
    # 왼쪽부터 다르면 누르기
    if button[i] != note[i]:
        cnt += 1
        
        # 범위 내 3개 누르기
        for j in range(3):
            if i + j < n:
                button[i+j] ^= 1

print(cnt)