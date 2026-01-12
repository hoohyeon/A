def dfs(number, last_digit):
    descending.append(number)

    # 마지막 숫자가 0이면 종료
    if last_digit == 0:
        return
        
    for next_digit in range(last_digit):
        dfs(number + str(next_digit), next_digit)

descending = []
for i in range(10):
    dfs(str(i), i)

# 오름차순 정렬
descending_list = sorted(list(map(int, descending)))

n = int(input())

if n - 1 < len(descending_list):
    print(descending_list[n-1])
else:
    print(-1)