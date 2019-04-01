tekst = "Anna, paweł, JuliA"

lista = tekst.split(", ")
print(tekst)
print(lista)

print(type(lista)) #class "list"

imie1 = lista[0]
print(imie1) #Anna

imieDuza = imie1.upper()
print(imieDuza) #ANNA

imieMala = imie1.lower()
print(imieMala) #anna

#sprawdzenie zawartosci
nazwisko = ""
print(nazwisko.isalpha()) #false

print("\nPodaj swoje nazwisko: ", end="")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc) #True or False

text1 ="\nJulia\n"
text2 = "Nowak"
text1 = text1.rstrip()
print (text1 + text2)
print(text1 + " " + text2)

#wyswietlanie lancucha znakow

#wszystkie wersje Pythona
#text1 = "%s, Java i %s" & ("PHP" + "Python")
#print(text1)

#nowsze wersje Pythona
text = "{1}, Java i {0}".format("PHP", "Python", "JAVA")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisanie danych
rok = 2019
miesiac = "kwiecień"
dzien = 1

print("\nData: ", end="")
print(dzien, miesiac, rok)

print("\nData: ", end="")
print(dzien, miesiac, rok, sep="-")

print()
