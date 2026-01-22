import sys, heapq
input = sys.stdin.readline

n = int(input())
meeting = [tuple(map(int, input().split())) for _ in range(n)]
meeting.sort()

max_room = 0
end_time = []

for s, e in meeting:
    # 끝난 회의 전부 정리
    while end_time and end_time[0] <= s:
        heapq.heappop(end_time)

    heapq.heappush(end_time, e)

    max_room = max(max_room, len(end_time))

print(max_room)