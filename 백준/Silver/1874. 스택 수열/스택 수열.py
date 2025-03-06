import sys
input = sys.stdin.readline

n = int(input())
target_sequence = [int(input()) for _ in range(n)]

stack = []
next_push = 1
result = []

for number in target_sequence:
    # 현재 목표 숫자와 스택의 최상위 숫자가 일치하지 않을 때
    while next_push <= n and (not stack or stack[-1] != number):
        stack.append(next_push)  # 숫자 push
        result.append('+')  # push 연산 기록
        next_push += 1  # 다음 숫자로 증가

    # 스택의 최상위 숫자가 목표 숫자와 일치하는 경우 pop
    if stack and stack[-1] == number:
        stack.pop()  # 숫자 pop
        result.append('-')  # pop 연산 기록
    else:
        print("NO")  # 수열을 만들 수 없는 경우
        break
else:
    # 모든 숫자를 성공적으로 처리한 경우
    print('\n'.join(result))  # 연산 기록 출력
