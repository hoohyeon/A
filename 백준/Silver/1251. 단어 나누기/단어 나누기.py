s = input()
n = len(s)
l = []

for i in range(1, n-1):
    for j in range(i+1, n):
        a, b, c = s[:i], s[i:j], s[j:]

        w = a[::-1] + b[::-1] + c[::-1]
        l.append(w)

l.sort()

print(l[0])