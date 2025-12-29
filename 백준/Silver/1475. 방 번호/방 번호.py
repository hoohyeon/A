N = input()

# cards[i] = i번 숫자가 필요한 개수
cards = [0] * 10

for n in N:
    if n == '6' or n == '9':
        if cards[6] <= cards[9]:
            cards[6] += 1
        else:
            cards[9] += 1
    else:
        cards[int(n)] += 1
    
print(max(cards))