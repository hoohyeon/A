n = int(input())
dice = list(map(int, input().split()))

if n == 1:
    print(sum(dice) - max(dice))

else:
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    
    min_list = [min(a, f), min(b,e), min(c, d)]
    min_list.sort()
    
    min1 = min_list[0]
    min2 = min_list[0] + min_list[1]
    min3 = min_list[0] + min_list[1] + min_list[2]
    
    min_sum = min3 * 4 + min2 * (8 * n - 12) + min1 * (5 * n ** 2 - 16 * n + 12)
    
    print(min_sum)