while True:
    side = list(map(int, input().split()))

    side.sort()
    
    a, b, c = side[0], side[1], side[2]

    # 종료 조건
    if a == 0 and b == 0 and c == 0:
        break

    # 삼각형 X
    if a + b <= c:
        print('Invalid')
    
    elif a == b == c:
        print('Equilateral')

    elif a == b != c or a != b == c:
        print('Isosceles')

    elif a != b != c:
        print('Scalene')