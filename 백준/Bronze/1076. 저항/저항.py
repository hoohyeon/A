r = {
    'black' : 0,
    'brown' : 1,
    'red' : 2,
    'orange' : 3,
    'yellow' : 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey' : 8,
    'white' : 9
}

first = input()
second = input()
third = input()

result = (10 * r[first] + r[second]) * (10 ** r[third])

print(result)