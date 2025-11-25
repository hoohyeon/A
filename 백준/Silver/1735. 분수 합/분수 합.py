import math

a, b = map(int, input().split())
c, d = map(int, input().split())

e = a * d + c * b
f = b * d

g = math.gcd(e, f)

print(int(e/g), int(f/g))