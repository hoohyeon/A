s = input()

count = [0] * 26
for ch in s:
    index = ord(ch) - ord('a')
    count[index] += 1

def dfs(prev_char, str_len):
    if str_len == len(s):
        return 1

    cnt = 0
    for next_char in range(26):
        if next_char != prev_char and count[next_char] > 0:
            count[next_char] -= 1
            cnt += dfs(next_char, str_len + 1)
            count[next_char] += 1
    return cnt
    
lucky = dfs(-1, 0)

print(lucky)