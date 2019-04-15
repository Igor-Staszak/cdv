#listy
programowanie = ['PHP', 'Python', 'Java']
print(type(programowanie))
programowanie.append('C#')
programowanie.append('PHP')
print(programowanie)

ile = programowanie.count('PHP')
print(f'Ile razy jest "PHP": {ile}')

ile = programowanie.count('php')
print(f'Ile razy jest "php": {ile}')


#tuple
imiona = ('Julia', 'Anna', 'Tomek')
print(imiona)
print(type(imiona))


#slowniki
osoba = {
  'imie':'Julia',
  'nazwisko':'Kowalska',
  'wiek':23
}

print(osoba)
print(type(osoba))

print(osoba['imie'])
print(osoba.keys())

print(osoba.get('wzrost', 'brak danych'))


#################################################################


'''
  Utworz slownik i przyhpisz mu trzy imiona podane z klawiatury
  Wyswietl te dane,
  imie1: ...
  imie2: ...
  imie3: ...
'''

x = input('Podaj pierwsze imie: ')
y = input('Podaj drugie imie: ')
z = input('Podaj trzecie imie: ')

imionaSlownik = {
  '0':x,
  '1':y,
  '2':z
}

print(imionaSlownik)
