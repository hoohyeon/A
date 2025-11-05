n, m = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_c = arr_a + arr_b

arr_c.sort()

print(*arr_c)