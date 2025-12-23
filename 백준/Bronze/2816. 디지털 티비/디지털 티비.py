n = int(input())
channels = [input() for _ in range(n)]

cursor = 0
buttons = ''

# KBS1 첫 번째로
while channels[cursor] != 'KBS1':
    cursor += 1
    buttons += '1'

while cursor > 0:
    channels[cursor], channels[cursor-1] = channels[cursor-1], channels[cursor]
    cursor -= 1
    buttons += '4'

# KBS2 두 번째로
while channels[cursor] != 'KBS2':
    cursor += 1
    buttons += '1'

while cursor > 1:
    channels[cursor], channels[cursor-1] = channels[cursor-1], channels[cursor]
    cursor -= 1
    buttons += '4'

print(buttons)