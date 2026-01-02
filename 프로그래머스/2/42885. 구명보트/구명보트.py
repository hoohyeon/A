def solution(people, limit):
    
    people.sort()
    
    left = 0
    right = len(people) - 1
    boat = 0
    
    while left <= right:
        # 가장 가벼운 사람 + 가장 무거운 사람 <= 무게 제한
        # 가장 가벼운 사람 태우기
        if people[left] + people[right] <= limit:
            left += 1
        
        # 가장 무거운 사람은 무조건 태우기
        right -= 1
        boat += 1
        
    return boat