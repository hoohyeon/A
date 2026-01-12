N = int(input())
S, B = [], []
for _ in range(N):
    s, b = map(int, input().split())
    S.append(s)
    B.append(b)

answer = int(1e9)
def dfs(idx, sour, bitter, used):
    global answer
    
    # 재료 끝까지 보고, 하나라도 사용했으면
    if idx == N:
        if used:
            answer = min(answer, abs(sour - bitter))
        return

    # 다음 재료 사용, 사용 X
    dfs(idx+1, sour * S[idx], bitter + B[idx], True)
    dfs(idx+1, sour, bitter, used)

dfs(0, 1, 0, False)

print(answer)