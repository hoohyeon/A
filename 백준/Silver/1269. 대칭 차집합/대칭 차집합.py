a, b = map(int, input().split())

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

s1 = set(l1)
s2 = set(l2)

s3 = s1 - s2
s4 = s2 - s1

print(len(s3) + len(s4))