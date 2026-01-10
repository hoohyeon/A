n = int(input())
scores = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n-2, -1, -1):
    # 다음 레벨 점수보다 크면 그 점수보다 1점 낮게
    if scores[i] >= scores[i+1]:
        cnt += (scores[i] - scores[i+1]) + 1
        
        scores[i] = scores[i+1] - 1
        
print(cnt)