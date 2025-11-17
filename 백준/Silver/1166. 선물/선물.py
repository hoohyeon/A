n, l, w, h = map(int, input().split())

s, e = 0, max(l, w, h)

for _ in range(100):
    
    m = (s + e) / 2
    cnt = (l // m) * (w // m) * (h // m)
    
    if cnt >= n:
        s = m

    else:
        e = m

print(f"{s:.10f}")