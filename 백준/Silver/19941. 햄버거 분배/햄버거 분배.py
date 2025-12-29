n, k = map(int, input().split())
table = list(input())

# 먹는 사람 위치
eat = [0] * n

for i in range(n):
    # 사람 위치
    if table[i] == 'P':      
        # 닿을 수 있는 거리 범위
        for j in range(i-k, i+k+1):
            # 닿을 수 있는 거리가 테이블 내
            if j >= 0 and j < n:
                # 가장 왼쪽에 있는 햄버거부터 먹으면
                if table[j] == 'H':
                    eat[i] = 1
                    table[j] = 0
                    break
                
print(sum(eat))