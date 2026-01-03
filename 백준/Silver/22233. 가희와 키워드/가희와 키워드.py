import sys
input = sys.stdin.readline

n, m = map(int, input().split())

keyword = set(input().strip() for _ in range(n))

for _ in range(m):
    for w in input().strip().split(','):
        keyword.discard(w)
    
    print(len(keyword))