s = input()
n = len(s)

suffixs = []
for i in range(n):
    suffixs.append(s[i:])

for suffix in sorted(suffixs):
    print(suffix)