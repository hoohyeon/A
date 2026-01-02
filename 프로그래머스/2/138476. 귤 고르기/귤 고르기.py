from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    
    # sorted = list
    count = sorted(counter.values(), reverse = True)
    
    # 귤 개수, 종류 수 
    total, kind = 0, 0
    for c in count:
        total += c
        kind += 1
        
        if total >= k:
            break
    
    answer = kind
    
    return answer