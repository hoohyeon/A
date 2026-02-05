docs = input()
find = input()

idx = 0
cnt = 0

while idx < len(docs):
    if docs[idx:idx+len(find)] == find:
        cnt += 1
        idx += len(find)
    
    else:
        idx += 1
    
print(cnt)