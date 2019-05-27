#przekazywanie argumentow przez referencje
def show(name):
  print(f'Przed modyfikacja: {name}')
  name[0] = 'Beata'
  name[1] = 'Barbara'
  name[2] = 'Bogdan'
  print(f'Po modyfikacji: {name}')
  print(f'ID Po modyfikacji: {id(name)}')

data = ['Anna','Agnieszka','Andrzej']
print(f'Przed wywołaniem funkcji show: {data}')
print(f'ID obiektu przed wywołaniem funkcji show: {id(data)}')
print()
print()
show(data)
print(f'Po wywołankiu funkcji show: {id(data)}')


#słownik
print()
print()
data1 = {0: 'Artur', 1: 'Andrzej'}
print(f'ID przed modyfikacją (słownik): {id(data1)}')
show(data1)


#przekazywanie argumentow przez wartosc
print()
print()
def show1(city):
  print(f'Przed modyfikacja: {city}')
  city[0] = 'Berlin'
  city[1] = 'Londyn'
  print(f'Po modyfikacji: {city}')
  print(f'ID Po modyfikacji: {id(city)}')


miasto = ['Gniezno', 'Poznan']

print(f'Przed wywolaniem funkcji show1: {miasto}')
print(f'ID obiektu przed wywolaniem funkcji show1: {id(miasto)}')
show1(list(miasto))
print(f'Po wywolaniu funkcji show1: {miasto}')


#slownik
print()
print()
miasto1 = {
  0: 'Gniezno',
  1: 'Poznań'
}

print(f'Przed wywolaniem funkcji show1: {miasto1}')
print(f'ID obiektu przed wywolaniem funkcji show1: {id(miasto1)}')
show1(dict(miasto1))
print(f'Po wywolaniu funkcji show1: {miasto1}')
print()
print()
print()


########################################
def div(x, y):
  try:
    result = x / y
    print(f'{x}/{y}={result}')
  except ZeroDivisionError:
    print(f'Error, nie wolno dzielic przez 0')

div(4,2)
