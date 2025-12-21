n = int(input())

# col[c] = c열에 퀸 여부
col = [False] * n

# diag[i] = i번째 대각선 퀸 여부
diag1 = [False] * (2*n-1)
diag2 = [False] * (2*n-1)

# 경우의 수
cnt = 0
def dfs(r):
    global cnt
    
    if r == n:
        cnt += 1
        return cnt
    
    # r 행, c 열에 놓을 수 있는 지
    for c in range(n):
        
        # d1, d2 번째 대각선 인덱스
        d1 = r - c + (n - 1)
        d2 = r + c
        
        # 열과 대각선에 퀸이 없다면
        # if not (col[c] or diag1[d1] or diag2[d2]) : 하나라도 사용 X
        if not col[c] and not diag1[d1] and not diag2[d2]:
            # 퀸 놓기
            col[c], diag1[d1], diag2[d2] = True, True, True
            # 다음 열
            dfs(r+1)
            # 퀸 빼기
            col[c], diag1[d1], diag2[d2] = False, False, False
            
# 0번째 열 시작
dfs(0)

print(cnt)