import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# key = 단어, value = 빈도
word_dict = {}
for _ in range(n):
    word = input().strip()
    
    # 길이가 m 이상
    if len(word) >= m:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            
# 단어장 / 빈도, 길이, 단어 순으로 정렬
wordbook = sorted(word_dict.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for k, v in wordbook:
    print(k)