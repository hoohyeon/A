n = int(input())

books = {}

for _ in range(n):
    title = input()

    if title in books:
        books[title] += 1

    else:
        books[title] = 1

best = sorted(books.items(), key= lambda x:(-x[1], x[0]))

print(best[0][0])