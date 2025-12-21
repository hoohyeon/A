from collections import deque

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = deque([0] * W)

t = 0
current_weight = 0

while bridge:
    # 시간 증가    
    t += 1
    
    # 트럭 지나가기
    out = bridge.popleft()
    current_weight -= out
    
    # 건널 트럭 있으면
    if trucks:
        # 다음 트럭이 올라갈 수 있으면
        if current_weight + trucks[0] <= L:
            next_truck = trucks.pop(0)
            # 다리에 올라가고
            bridge.append(next_truck)
            # 하중 증가
            current_weight += next_truck
        
        # 다음 트럭이 올라갈 수 없으면
        # 0으로 채우기
        else:
            bridge.append(0)
    
print(t)