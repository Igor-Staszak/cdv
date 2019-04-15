#print("Podaj x - ", end="")
#x = input()
#x = int(x)
x = 5

if x == 5:
  print("Wartosc x jest rowne 5")
  x = str(x)
  print("x = " + x)       #trzeba przekonwertowac, by wypisalo w konkatenacji
  print("x =", x)
else:
  print("Wartosc  jest rozna od 5")
  print("x =", x)

########################################

y = True          #prawda

if y:
  print("prawda")
else:
  print("falsz")

########################################

#j = '1'
#j = '0'
j = '' #false dopiero
#j = False #i teraz
if bool(j):
  print('true')
else:
  print('false')

########################################

k = input('Podaj wartosc dla zmiennej k: ')
k = float(k)

if bool(k):
  print('true')
else:
  print('false')

########################################

