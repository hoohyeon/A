import sys
input = sys.stdin.readline

n = int(input())
log = set()

for _ in range(n):
    name, enter_leave = input().split()
    
    if enter_leave == 'enter':
        log.add(name)

    # leave
    else:
        log.remove(name)
        
for person in sorted(log, reverse=True):
    print(person)