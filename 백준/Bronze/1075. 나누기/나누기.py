n = int(input())
f = int(input())

a = (n // 100) * 100 
b = a % f

if b == 0:
    print('00')

else:
    r = f - b

    if r < 10:
        print('0' + str(r))
    
    else:
        print(r)