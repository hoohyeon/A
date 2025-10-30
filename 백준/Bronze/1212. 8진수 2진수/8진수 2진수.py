octal = input()

binary = ''

octal_binary = {
    '0' : '000',
    '1' : '001',
    '2' : '010',
    '3' : '011',
    '4' : '100',
    '5' : '101',
    '6' : '110',
    '7' : '111'
}

binary_parts = [octal_binary[ch] for ch in octal]

binary = ''.join(binary_parts)

binary = binary.lstrip('0')

print(binary if binary else '0')