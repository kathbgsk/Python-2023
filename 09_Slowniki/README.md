# 9. Słowniki (`dict`)

- Tworzenie słowników
  - Pobieranie wartości ze słowników
  -  Modyfikacja zawartości słowników
- Iteracje
- https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
---
# Zadania

- Dla listy napisów pobranej w pętli z wejścia wypisać słownik ilości wystąpień napisów
  - np. dla `['Ala', 'ma' 'kota', 'kota']` wypisać `{'Ala': 1, 'ma': 1, ;'kota': 2}`
- Dla wczytanej liczby z wejścia z zakresu 1-999 wypisać jej postać słowną
  - np. dla `73` wypisać `siedemdziesiąt trzy`


nazwy_jednosci = {0: "zero", 1:"jeden", 2: "dwa", 3" "trzy", 4: "cztery", 5: "piec", 6: "szesc", 7:"siedem", 8:"osiem", 9: "dziewiec"}
dziesiatki:{10: "dziescisc", 20: "dwadziescia", 30: "trzydziesc", 40:"zec", 50:"jdhsdkfh" 6:"nvkfjvn" 70:"vjhfvj", 80:"fkjvnjkdf", 90: "jhghg"
nastki: ={11: "jednenascie", 12:"dwanascie:, 13:"trzynscie:, 14:"czternascie", 15:"pietnascie", 16:"szczesnascie",17:"siedemnascie", 18: "osiemscie", 19: "dziewietnascie"}
while = input ("liczba z zakresu")

slownik = {}
napis = dziesiatki[n - n%10] + " " = nazwa_jednosci [n % 10]

print (napis)






nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
dziesiatki = {10: "dziesiec", 20: "dwadziescia", 30: "trzydziesci", 40: "czterdziesci", 50: "piecdziesiat",
              60: "szescdziesiat", 70: "siedemdziesiat", 80: "osiemdziesiat", 90: "dziewiecdziesiat"}

nastki = {11: "jedenascie", 12: "dwanascie", 13: "trzynascie", 14: "czternascie", 15: "pietnascie",
          16: "szesnascie", 17: "siedemnascie", 18: "osiemnascie", 19: "dziewietnascie"}

slownik = {}

n = int(input("Wpisz liczbe:"))
if n in range(11, 20):
    napis = nastki[n]
else:
    napis = dziesiatki[n - n % 10] + " " + nazwy_jednosci[n % 10]

print(napis)