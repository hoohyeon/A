s = input()

# s의 인덱스
idx = 0
n = 1

# 인덱스가 끝까지 가면 종료
while idx < len(s):
    # 현재 인덱스에서 현재 n에서 쓸 수 있는 문자 여부 검사
    for ch in str(n):
        if idx < len(s) and s[idx] == ch:
            idx += 1
    n += 1

# 마지막에 +1 되므로 정답은 n-1
print(n-1)