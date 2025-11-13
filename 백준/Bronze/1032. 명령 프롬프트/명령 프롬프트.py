n = int(input())
commands = [input() for _ in range(n)]

first_command = commands[0]
command_len = len(first_command)
prompt = list(first_command)

for i in range(1, n):
    compare_command = commands[i]
    for j in range(command_len):
        if first_command[j] != compare_command[j]:
            prompt[j] = '?'

print(''.join(prompt))