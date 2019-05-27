#zad 1
def expDiv():
  try:
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))
    result = ((a*a+b)/((a+b)*(a+b)))
    print(f'Wynik: {result}')
  except:
    print(f'Error')

#expDiv()


#zad 2
def expCount():
  try:
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))
    c = float(input('Podaj c: '))
    if c > 0:
      result = a*a+b
      print(f'c > 0 // {a}^2 + {b} = {result}')
    elif c < 0:
      result = a-b*b
      print(f'c < 0 // {a}-{b}^2 = {result}')
    elif c == 0:
      result = 1/(a-b)
      print(f'c == 0 // 1/({a}-{b}) = {result}')
  except:
    print('Error xD')

#expCount()


#zad 3 EUKLIDES
def nwd():
  try:
    a = int(input('Podaj a: '))
    b = int(input('Podaj b: '))

    while b > 0:
      c = a & b
      a = b
      b = c
    print(a)
  except:
    print('Error')

nwd()
