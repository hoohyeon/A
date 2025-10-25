n, m = map(int, input().split())

numbers = [i for i in range(2, n+1)]

erase = []

while numbers:
    p = numbers[0]
    temp = []
    
    for number in numbers:
        if number % p == 0:
            erase.append(number)
        else:
            temp.append(number)
            
    numbers = temp
        
print(erase[m-1])