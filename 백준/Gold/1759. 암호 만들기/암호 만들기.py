l, c = map(int, input().split())
letter = list(input().split())
letter.sort()

def dfs(start, cnt, password):
    if cnt == l:
        vowel, consonant = 0, 0
        for ch in password:
            if ch in 'aeiou':
                vowel += 1
            else:
                consonant += 1

        if vowel >= 1 and consonant >= 2:
            print(password)

    for i in range(start, c):
        dfs(i+1, cnt+1, password + letter[i])

dfs(0, 0, "")