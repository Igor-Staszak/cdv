def wyswietl(num1, num2):
  print(f'Liczba1: {num1}')
  print(f'Liczba2: {num2}')

wyswietl(2, 4)
print()
print()


#args
def wyswietlArgs(num1, *args):
  print(f'Pierwszy element: {num1}')
  for i in args:
    print(f'Args: {i}')

wyswietlArgs(2,3,4,5)
print()
print()

#kwargs
def pracownik(**kwargs):
  print(kwargs)

pracownik1 = {
  'fName' : 'Janusz',
  'lName' : 'Nowak',
  'age' : 23,
  'city' : 'Poznan',
  'job' : True
}

pracownik(**pracownik1)
print()
print()

##############################
def pracownik(**kwargs):
  for key, val in kwargs.items():
    print(f'Klucz: {key}, wartość: {val}')

pracownik1 = {
  'fName' : 'Janusz',
  'lName' : 'Nowak',
  'age' : 23,
  'city' : 'Poznan',
  'job' : True
}

pracownik(**pracownik1)
print()
print()
