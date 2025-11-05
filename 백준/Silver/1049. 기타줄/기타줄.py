n, m = map(int, input().split())

package, each = [], []

for _ in range(m):
    
    p, e = map(int, input().split())
    
    package.append(p)
    each.append(e)
    
p = min(package)
e = min(each)

result = min(n//6 * p + n % 6 * e, (n//6 + 1) * p, n * e)

print(result)