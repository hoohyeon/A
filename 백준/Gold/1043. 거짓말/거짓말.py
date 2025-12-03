n, m = map(int, input().split())
t_num, *t_list = map(int, input().split())
p_list = [list(map(int, input().split()[1:])) for _ in range(m)]
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra

for party in p_list:
    if len(party) >= 2:
        first = party[0]
        for person in party[1:]:
            union(first, person)

truth_roots = set(find(x) for x in t_list)

cnt = 0
for party in p_list:
    if not any(find(person) in truth_roots for person in party):
        cnt += 1

print(cnt)