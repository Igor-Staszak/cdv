#definicja funkcji
def witaj():
  print('Witaj', end = " ")
  print('Janusz!')

#wyswietlanie funkcji
witaj()

def wyswietlWiek(wiek):
  print(f'Twoj wiek: {wiek}')

wyswietlWiek(23)


def iloczyn(a, b):
  return a * b

print(f'Iloczyn wynosi: {iloczyn(3, 4)}')

def iloraz(a, b):
  return a / b

x = iloraz(4, 5)
print(f'Iloraz wynosi: {x}')
print(type(x))

print(iloraz(b=10, a=3))

print('\n\n\n\n')
'''
Uzytkownik podaje z klwiatury:
marka, model, pojemnosc, predkoscMax
utworz funkcje, ktora pobierze dane od uzytkownika i przypisze do slownika
utworz druga funkcje wyswietlajaca dane w formacie:
Marka: ...
Model: ...
Pojemnosc: ...
Predkosc maksymalna: ...
'''

samochod = {
  'Marka':'',
  'Model':'',
  'Pojemnosc':'',
  'Vmax':''
  }

def pobierzDane():
  marka1 = input('Podaj marke: ')
  model1 = input('Podaj model: ')
  pojemnosc1 = input('Podaj pojemnosc: ')
  vmax1 = input('Podaj predkosc maksymalna: ')

  samochod['Marka'] = marka1
  samochod['Model'] = model1
  samochod['Pojemnosc'] = pojemnosc1
  samochod['Vmax'] = vmax1

def wyswietlDane():
  print('Marka: ', samochod['Marka'])
  print('Model: ', samochod['Model'])
  print('Pojemnosc: ', samochod['Pojemnosc'])
  print('Predkosc maksymalna: ', samochod['Vmax'])

pobierzDane()
wyswietlDane()
