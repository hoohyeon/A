n = int(input())
tops = list(map(int, input().split()))

stack = [] # 아직 신호를 받을 수 있는 탑들
answer = []

for i in range(n):
    # 현재 탑보다 낮은 탑들은 제거
    while stack and tops[stack[-1]] < tops[i]:
        stack.pop()

    # 스택에 남아 있는 가장 가까운 왼쪽의 높은 탑
    # 1-based index
    if stack:
        answer.append(stack[-1] + 1)

    # 못 만나면 0
    else:
        answer.append(0)

    # 현재 탑도 후보로
    stack.append(i)

print(*answer)