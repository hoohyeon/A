import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

def f(trees, m):
    left, right = 0, max(trees)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        wood = sum(tree - mid for tree in trees if tree - mid >= 0)

        if wood >= m:
            result = mid
            left = mid + 1

        else:
            right = mid - 1

    return result

print(f(trees, m))