N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

min_protor = N
for a in A:
    
    a -= B
    
    # 부감독관 필요
    if a > 0:
        if a % C:
            min_protor += (a // C) + 1
            
        else:
            min_protor += (a // C)

print(min_protor)