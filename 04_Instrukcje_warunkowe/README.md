# 4. Instrukcje warunkowe

- Wyrażenie logiczne - coś co ma wartość `True` albo `False`
  - Porównanie `==`
  - Różny `!=`
  - Mniejszy, większy `<`, `>`
  - Mniejszy, większy  bądź równy `<=`, `>=`

- 1 Warunek logiczny - `if` <warunek logiczny> 
  - `if` `wyrażenie logiczne` `:`
    - dalej wcięcie - 4 spacje
    - kod do warunku wcięty
  - `else` - w przeciwnym wypadku
  - jak jest wiele warunków - to nie zagnieżdzamy tylko robimy else + if czyli `elif`
  - można budować złożone warunki przy pomocy `not`, `and` oraz `or`
  - jest operator `:=` od Pythona 3.8 pozwalający na przypisanie bezpośrednio w warunku
  

---
# Zadanie

- wczytaj liczbę 2 cyfrową - wypisz `Dobra liczba` jeśli suma jej cyfr dzieli się przez 7 oraz liczba jest parzysta, a `Zła liczba` w przeciwnym wypadku 



a= int(input("podaj liczbe"))
b = int (a/10)
c = a%10
i=b+c
if( i== 7 and a % 2 ==  0):
    print (f{i}"liczba jest dobra")
else:
    print (f{i}"liczba jest zla")

