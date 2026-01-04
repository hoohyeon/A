n = int(input())
base = input()

freq = [0] * 26
for ch in base:
    freq[ord(ch) - ord('A')] += 1
    
cnt = 0
for _ in range(n-1):
    word = input()
    freq2 = [0] * 26
    
    for ch2 in word:
        freq2[ord(ch2) - ord('A')] += 1
        
    diff = 0
    for i in range(26):
        diff += abs(freq[i] - freq2[i])

    # 알파벳 조합의 차이가 0이나 1이라면
    # 같은 단어, 비슷한 단어 (하나를 더하거나 뺀 경우)
    if diff == 0 or diff == 1:
        cnt += 1
    
    # 비슷한 단어 (하나를 다른 문자로 바꾼 경우)
    elif diff == 2 and len(word) == len(base):
        cnt += 1
        
print(cnt)