import sys
input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))

m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)

else:
    cnt = 0
    while boxes:
        for c in cranes:
            if boxes and c < boxes[-1]:
                continue
            
            for b in boxes:
                if c >= b:
                    boxes.remove(b)
                    break
        cnt += 1

    print(cnt)