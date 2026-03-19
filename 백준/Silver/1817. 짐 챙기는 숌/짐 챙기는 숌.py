n, m = map(int, input().split())

if n > 0:
    book = list(map(int, input().split()))

    # 현재 무게, 박스 개수
    now, cnt = 0, 1
    
    for i in range(n):
        # 현재 박스에 이번 책 넣을 수 있으면
        if now + book[i] <= m:
            now += book[i]
        
        # 없으면 새 박스
        else:
            cnt += 1
            now = book[i]
            
    print(cnt)
else:
    print(0)