#precyzje
x = "{0: 3f}".format(5)
print(x)

#napisz funkcje, ktora jako argument przyjmuje wartosc i zamienia dane po kursie dzisiejszym franka. wyswietl userowi ile frankow kupi za podana kwote

def plnToChf(value):
  kursChf = 3.81849933
  iloscChf = value / kursChf
  iloscChf = "{0: 1f}".format(iloscChf)
  print(f'Ilosc CHF: {iloscChf}')

plnToChf(500)
print()
print()

#zmienne globalne
zmiennaGlobal = 10
print(f'Wartosc zmiennej globalnej: {zmiennaGlobal}')
print(f'ID wartosci zmiennej globalnej: {id(zmiennaGlobal)}')
print()

def spr():
  global zmiennaGlobal
  zmiennaGlobal = 20
  print(f'Wartosc zmiennej globalnej wew funkcji: {zmiennaGlobal}')
  print(f'ID wartosci zmiennej globalnej wew funkcji: {id(zmiennaGlobal)}')

spr()
print()
print(f'Wartosc zmiennej globalnej: {zmiennaGlobal}')
print(f'ID wartosci zmiennej globalnej: {id(zmiennaGlobal)}')
