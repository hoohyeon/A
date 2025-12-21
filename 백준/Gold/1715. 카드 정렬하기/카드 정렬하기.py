import sys, heapq
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)

cnt = 0

# 카드 묶음이 1개 이상이면
while len(cards) > 1:
    # 먼저 합친 묶음 수만큼 계속 비교해야 하므로
    # 현재 묶음에서 카드 수가 적은 묶음부터 합치기
    
    # 현재 카드 수가 적은 두 묶음
    cnt1 = heapq.heappop(cards)
    cnt2 = heapq.heappop(cards)
    
    cnt += (cnt1 + cnt2)

    # 합친 묶음을 한 묶음으로
    heapq.heappush(cards, cnt1 + cnt2)
    
print(cnt)