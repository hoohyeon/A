import sys
input = sys.stdin.readline

n, m = map(int, input().split())

titles = []
limits = []

for _ in range(n):
    name, value = input().split()
    titles.append(name)
    limits.append(int(value))

for _ in range(m):
    power = int(input())
    
    left = 0
    right = n-1
    
    while left < right:
        mid = (left + right) // 2
        
        if limits[mid] >= power:
            right = mid
            
        else:
            left = mid + 1
            
    print(titles[left])