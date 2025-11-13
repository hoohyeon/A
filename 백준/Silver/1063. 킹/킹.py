king, stone, n = input().split()
n = int(n)
commands = [input() for _ in range(n)]

king_row_index = 8 - int(king[1])
king_col_index = ord(king[0]) - ord('A')

stone_row_index = 8 - int(stone[1])
stone_col_index = ord(stone[0]) - ord('A')

moves = {
    "R":  (0, 1),
    "L":  (0, -1),
    "B":  (1, 0),
    "T":  (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1)
}

r, c = king_row_index, king_col_index
sr, sc = stone_row_index, stone_col_index

for cmd in commands:
    dr, dc = moves[cmd]
    nr, nc = r + dr, c + dc

    if not (0 <= nr < 8 and 0 <= nc < 8):
        continue

    if (nr == sr) and (nc == sc):
        nsr, nsc = sr + dr, sc + dc

        if not (0 <= nsr < 8 and 0 <= nsc < 8):
            continue

        sr, sc = nsr, nsc
        r, c = nr,nc

    else:
        r, c = nr, nc

final_king_pos = chr(c + ord('A')) + str(8 - r)
final_stone_pos = chr(sc + ord('A')) + str(8 - sr)

print(final_king_pos)
print(final_stone_pos)