from collections import deque

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    
    s = input()
    arr = deque(eval(s))

    is_reversed = False
    error = False

    for cmd in p:
        if cmd == 'R':
            is_reversed = not is_reversed

        elif cmd == 'D':
            if not arr:
                print('error')
                error = True
                break
            else:
                if is_reversed:
                    arr.pop()
                else:
                    arr.popleft()

    if not error:
        if is_reversed:
            arr.reverse()

        print(f"[{','.join(map(str, arr))}]")