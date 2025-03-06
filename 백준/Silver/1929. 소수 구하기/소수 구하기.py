import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def f(x):
    if x == 1:
        return False
    
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    
    return True

for number in range(n, m+1):
    if f(number):
        print(number)
