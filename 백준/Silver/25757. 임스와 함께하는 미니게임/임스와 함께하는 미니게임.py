N, game = input().split()
n = int(N)

if game == 'Y':
    need_people = 1
    
elif game == 'F':
    need_people = 2
    
elif game == 'O':
    need_people = 3
    
played_people = set()
cnt, people = 0, 0

for _ in range(n):
    person = input()
    
    if person not in played_people:
        people += 1
        played_people.add(person)
        
        if people == need_people:
            cnt += 1
            people = 0
            
print(cnt)