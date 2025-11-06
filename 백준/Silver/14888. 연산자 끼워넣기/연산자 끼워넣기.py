n = int(input())
numbers = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_value, min_value = -int(1e9), int(1e9)
def dfs(idx, current, remain_ops):
    global max_value, min_value
    
    if idx == n:
        max_value = max(max_value, current)
        min_value = min(min_value, current)
        return

    for i in range(4):
        if remain_ops[i] > 0:
            remain_ops[i] -= 1
            next_val = calc(current, numbers[idx], i)

            dfs(idx+1, next_val, remain_ops)

            remain_ops[i] += 1

def calc(a, b, op_idx):
    if op_idx == 0:
        return a + b
    elif op_idx == 1:
        return a - b
    elif op_idx == 2:
        return a * b
    else:
        if a < 0:
            return -(-a//b)
        else:
            return a // b

dfs(1, numbers[0], ops)

print(max_value)
print(min_value)