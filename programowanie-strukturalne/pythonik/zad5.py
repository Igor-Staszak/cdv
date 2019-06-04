def ifFirst(num):
    isFirst1 = 0
    isFirst2 = 0
    for i in range(2, num):
        res = num % i
        if res == 0:
            isFirst1 = 1
        else:
            isFirst2 = 1

    if isFirst1 == 1:
        print(f'Liczba {num} nie jest liczba pierwsza')
    if isFirst2 == 1 and isFirst1 == 0:
        print(f'Liczba {num} jest liczba pierwsza')

numeric = input('Podaj liczbe naturalna: ')
numeric = int(numeric)
ifFirst(numeric)
