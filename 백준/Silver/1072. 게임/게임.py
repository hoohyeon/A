x, y = map(int, input().split())

z = (y * 100) // x

more_game = -1

left, right = 1, x

while left <= right:
    mid = (left + right) // 2

    new_z = ((y + mid) * 100 ) // (x + mid)

    if new_z > z:
        more_game = mid
        right = mid - 1
    
    else:
        left = mid + 1

print(more_game)