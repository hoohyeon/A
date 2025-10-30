t = int(input())

for _ in range(t):

    n = int(input())

    number_list = list(map(int, input().split()))

    print(min(number_list), max(number_list))