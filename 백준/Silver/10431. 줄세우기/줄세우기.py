p = int(input())

for _ in range(p):
    data = list(map(int, input().split()))
    t = data[0]
    students = data[1:]
    
    moves = 0
    
    # 이전 차례에 자기보다 큰 학생이 몇 명
    # i 학생이 줄을 설 때 걔네가 뒤로 가야하니까
    for i in range(len(students)):
        for j in range(i):
            if students[j] > students[i]:
                moves += 1
                
    print(t, moves)