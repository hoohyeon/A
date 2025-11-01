n = int(input())

extension = {}
for _ in range(n):
    file = input()
    
    ext = file.split('.')[-1]
    
    if ext in extension:
        extension[ext] += 1
    else:
        extension[ext] = 1    
    
for ext in sorted(extension):
    print(ext, extension[ext])