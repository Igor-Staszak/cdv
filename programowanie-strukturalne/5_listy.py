programowanie = ['Python', 'C#', 'JS', 'PHP', 'Java']

print(programowanie)
print(type(programowanie))

pierwszy = programowanie[0]
print('Pierwszy jezyk programowania:', pierwszy)

trzyElementy = programowanie[:3]
print('Trzy elementy:', trzyElementy)

ostatni = programowanie[-1]
print('Ostatni jezyk programowania:', ostatni)


#Dodanie nowego elementu do listy
programowanie.append('R')
programowanie.append('Python')
print(programowanie)


#Zliczanie elementow w liscie
ile = programowanie.count('Python')
print(f'Python wystepuje {ile} razy')


#ilosc elementow w naszej liscie
iloscElem = len(programowanie)
print(f'Ilosc elementow: {iloscElem}')


#laczenie listy
print(f'\nLaczenie list:\n{programowanie}')
inneJezyki = ['C', 'C++']
programowanie.extend(inneJezyki)
print(programowanie)


#czyszczenie listy
nowa = programowanie
print(f'Nowa lista: {nowa}')
nowa.clear()
print(f'Nowa lista (czysta): {nowa}')
print(f'Lista programowanie (czysta): {programowanie}')
