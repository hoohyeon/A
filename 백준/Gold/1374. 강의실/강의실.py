n = int(input())
events = []

for _ in range(n):
    _, s, e = map(int, input().split())
    events.append((s, 1))
    events.append((e, -1))

events.sort(key=lambda x: (x[0], x[1]))

room = 0
max_room = 0
for tiem, delta in events:
    room += delta
    max_room = max(max_room, room)

print(max_room)