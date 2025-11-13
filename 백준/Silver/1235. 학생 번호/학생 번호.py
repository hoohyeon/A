n = int(input())

student_number = [input() for _ in range(n)]
number_len = len(student_number[0])

for i in range(1, number_len):
    number_list = []
    
    for number in student_number:
        
        number_list.append(number[number_len-i:number_len])

    number_set = set(number_list)

    if len(number_list) == len(number_set):
        number_len = i
        break

print(number_len)