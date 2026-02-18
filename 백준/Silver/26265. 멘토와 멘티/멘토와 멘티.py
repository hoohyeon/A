n = int(input())
m = {}

for _ in range(n):
    mentor, menti = input().split()
    
    if not mentor in m:
        m[mentor] = []
        
    m[mentor].append(menti)
    
for mentor in sorted(m.keys()):
    for menti in sorted(m[mentor], reverse=True):
        print(mentor, menti)