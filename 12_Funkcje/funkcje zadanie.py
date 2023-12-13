#stworzyc słownik `{ 'first': funkcja1, 'second': funkcja2 }`, wczytać przez `input` klucz, wywołać funkcję

def f1(n="OK"):
    """
    Ta funkcja wypisuje 'OK'
    :return: OK
    """
    print(n)
def f2(x="NOK"):
    """
    Ta funkcja wypisuje 'NOK'
    :return: NOK
    """
    print(x)

s= {'f1':f1, 'f2': f2}

inp= input("Klucz f1 czy f2")
f=s[inp]
f()

#------------------------------------------------------------------------------------------------------------------------
# stworzyc funckcję `alphabet_range` działająca jak `range` ale dla liter (z trzema parametrami - `start`, `end`, `step`)
#przykład: `alphabet_range('E')` -> `['A', 'B', 'C', 'D']` - albo jeszcze lepiej generator użyć
#`ord` - podaje kod calkowity danego znaku
# `chr` - podaje znak odpowiadający danemu kodowi całkowitemu

def alphabet_range (start="A", end ="z", step=1):

    return (chr(x) for x in range(ord(start), ord(end), step))

#lphabet_range("a", "f1", 1)

list(alphabet_range(end="M"))

#-----------------------------------------------------------------------------------------------------------------------
def alphabet_range (start="A", end ="z", step=1):
    return [chr(x) for x in range(ord(start), ord(end), step))
alphabet_range("a","f1",1)

#----------------------------------------------------------------

- stworzyćfunkcję`slownie_do999()`którazwrócisłownieliczbęzzakresu0 - 999
- stworzyćfunkcjępomocniczą`_slownie_do999()`zwracającąlistętupli`(wartość, słownie)`dla1i"nastek", 10, 100
- stworzyćfunkcjępomocniczą`_sklej()`sklejającąw / wlistę
- zbudowaćfunkcję`słownie`podającąsłownieliczbycałkowitedomiliardów(do`999_999_999_999`)

def slownie999(n):

    nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem",
                      8: "osiem",
                      9: "dziewięć"}
    nazwy_dziesiatki = {10: "dziesiec", 20: "dwadziescia", 30: "trzydziesci", 40: "czterdziesci", 50: "piecdziesiat",
                  60: "szescdziesiat", 70: "siedemdziesiat", 80: "osiemdziesiat", 90: "dziewiecdziesiat"}

    nazwy_nastki = {11: "jedenascie", 12: "dwanascie", 13: "trzynascie", 14: "czternascie", 15: "pietnascie",
              16: "szesnascie", 17: "siedemnascie", 18: "osiemnascie", 19: "dziewietnascie"}

    ret =[]

    jednosci = n%10
    nazwy_dziesiatki =n % 100 - jednosci
    setki = n - dziesiatki - jednosci

    if setki:
        ret.append(setki, nazwy_setki[setki])
    if dziesiatki ==1 and jednosci>0:
        nastki=10+jednosci
        ret.append(nastki, nazwy_nastki[nastki]))
    else:
        if dziesiatki:
        ret.append((dziesiatki,nazwy_dziesiatki[dziesiatki]))
        if jednosci((jednosci, nazwy_jednosci[jednosci]))

    return ret



print(_slownie999(3))
print(_slownie999(33))
print(_slownie999(3333))