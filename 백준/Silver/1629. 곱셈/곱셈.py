a, b, c = map(int, input().split())

def f(x, y, z):
    
    if y == 1:
        return x % z
    

    else:
        half = f(x, y // 2, z)
        
        if y % 2 == 0:
            return half * half % c
    
        else:
            return a * half * half % c

print(f(a, b, c))