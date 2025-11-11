L = int(input())
S = list(map(int, input().split()))
n = int(input())

S.sort()

if n in S:
    print(0)

else:
    left, right = 0, 0
    
    for num in S:
        if num < n:
            left = num
        elif num > n and right == 0:
            right = num
            
    left += 1
    right -= 1
    
    cnt = (n - left) * (right - n + 1) + (right - n)

    print(cnt)