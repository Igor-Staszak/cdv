def nwd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

num1 = input('Podaj liczbe a: ')
num1 = int(num1)
num2 = input('Podaj liczbe b: ')
num2 = int(num2)
print(f'NWD({num1}, {num2}): {nwd(num1, num2)}')
