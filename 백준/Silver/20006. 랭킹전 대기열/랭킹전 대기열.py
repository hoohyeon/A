p, m = map(int, input().split())

rooms = []

for _ in range(p):
    l, name = input().split()
    level = int(l)
    
    # 방 입장 여부
    placed = False
    
    for room in rooms:
        # 방 레벨
        room_level = room[0][0]
        
        # 이번 방 입장 가능 여부
        if abs(level - room_level) <= 10 and len(room) < m:
            room.append((level, name))
            placed = True
            break
    
    # 아무 방 입장 X : 새로운 방 생성
    if not placed:
        rooms.append([(level, name)])
        
for room in rooms:
    if len(room) == m:
        print('Started!')
        
    else:
        print('Waiting!')
    
    # 닉네임 정렬
    for level, name in sorted(room, key=lambda x:x[1]):
        print(level, name)