n = int(input())

cnt = 0
for _ in range(n):
    chat = input()
    
    if chat == 'ENTER':
        people = set()
        
    else:
        if not chat in people:
            people.add(chat)
            cnt += 1
        
print(cnt)