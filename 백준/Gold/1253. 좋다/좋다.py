n = int(input())
nlist = list(map(int, input().split()))
nlist.sort()
cnt = 0

for i in range(n):
    target = nlist[i]

    left, right = 0, n-1
    while left < right:
        if left == i:
            left += 1
            continue

        if right == i:
            right -= 1
            continue
            
        # 현재 포인터들의 합
        s = nlist[left] + nlist[right]

        # 합이 작으면 left += 1 (target 크게)
        if target > s:
            left += 1

        # 합이 크면 right -= 1 (target 작게)
        elif target < s:
            right -= 1

        # target == s
        else:
            cnt += 1
            break

print(cnt)