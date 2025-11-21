from collections import Counter

name = input()

count = Counter(name)

odd_chars = [ch for ch, cnt in count.items() if cnt % 2 == 1]

if len(odd_chars) > 1:
    print("I'm Sorry Hansoo")

else:
    p = ''
    
    for ch in sorted(count.keys()):

        p += ch * (count[ch] // 2)


    if odd_chars:
        print(p + odd_chars[0] + p[::-1])

    else:
        print(p + p[::-1])