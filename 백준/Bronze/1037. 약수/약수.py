n = int(input())

num_list = list(map(int, input().split()))

num_list.sort()

l = len(num_list)

if l == 1:
    ans = num_list[0] ** 2
    
else:
    ans = num_list[0] * num_list[-1]
    
print(ans)