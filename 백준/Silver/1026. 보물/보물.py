n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

new_a = sorted(a)
new_b = sorted(b, reverse=True)

new_list = [new_a[i] * new_b[i] for i in range(n)]
print(sum(new_list))    