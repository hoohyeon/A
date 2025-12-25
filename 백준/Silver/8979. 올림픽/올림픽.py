N, K = map(int, input().split())

medals = {}
for _ in range(N):
    country, gold, silver, bronze = map(int, input().split())
    
    medals[country] = (gold, silver, bronze)
    
# 1등 시작
cnt = 1
for country_id, medal in medals.items():
    # 파이썬 튜플 비교
    if medal > medals[K]:
        cnt += 1
        
print(cnt)