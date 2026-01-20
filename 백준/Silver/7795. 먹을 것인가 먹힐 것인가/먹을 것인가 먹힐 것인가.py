t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    cnt = 0
    
    # 각 i마다 A[i] > B[j] 만족하는 j의 개수
    # i, j : 0에서부터 증가 방향
    j = 0
    for i in range(n):
        while j < m and A[i] > B[j]:
            j += 1

        cnt += j
        
    print(cnt)