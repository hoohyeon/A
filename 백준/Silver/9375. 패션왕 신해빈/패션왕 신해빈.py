import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    category_dict = {}
    
    n = int(input())

    for _ in range(n):
        name, category = input().split()

        if category not in category_dict:
            category_dict[category] = []

        category_dict[category].append(name)

    choice = 1
    for category in category_dict:
        choice *= len(category_dict[category]) + 1

    choice -= 1

    print(choice) 