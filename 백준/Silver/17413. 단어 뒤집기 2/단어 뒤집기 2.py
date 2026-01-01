S = input()

result = []
parts = []
in_tag = False

for ch in S:
    # 태그 시작
    if ch == '<':
        if parts:
            result.extend(reversed(parts))
            parts.clear()
        in_tag = True
        result.append(ch)
    
    # 태그 종료
    elif ch == '>':
        in_tag = False
        result.append(ch)
        
    # 태그 안 - 바로 result
    elif in_tag:
        result.append(ch)
        
    # 공백 - parts 종료
    elif ch == ' ':
        result.extend(reversed(parts))
        parts.clear()
        result.append(' ')
    # 태그 밖 - parts 추가
    else:
        parts.append(ch)

# 남아있는 parts
if parts:
    result.extend(reversed(parts))
        
print(''.join(result))