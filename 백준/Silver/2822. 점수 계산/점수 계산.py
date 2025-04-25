score_list = []

for i in range(1, 9):
    score = int(input())
    score_list.append((score, i))
    
score_list.sort(reverse=True)

top_5 = score_list[:5]

total_score = sum(score for score, idx in top_5)

top5_indices = sorted(idx for score, idx in top_5)

print(total_score)
print(*top5_indices)