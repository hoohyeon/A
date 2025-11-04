def solution(numbers):
    
    n = len(numbers)
    
    answer = [-1] * n
    next_idx = [-1] * n
    
    for i in range(n-2, -1, -1):
        
        j = i + 1
        
        while j != -1 and (numbers[i] >= numbers[j]):
            j = next_idx[j]
            
        next_idx[i] = j
        
        if j != -1:
            answer[i] = numbers[next_idx[i]]

    return answer