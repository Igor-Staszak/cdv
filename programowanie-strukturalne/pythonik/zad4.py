def separate(num):
    listNum = list(num)
    listNum = [int(i) for i in listNum]
    res = 0

    for j in range(0, len(listNum)):
        res = res + listNum[j]
        print(f'res = {res}, listNum[{j}] = {listNum[j]}')
    return res

numeric = input('Podaj liczbe naturalna: ')
print(f'Wynik dodawania wynosi: {separate(numeric)}')
