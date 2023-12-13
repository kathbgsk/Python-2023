import sys
import os

if __name__ == '__main__':
    print(f'Jestem w {os.getcwd()}')
    print(f'A to moje argumenty z linii poleceń {sys.argv}')


#_______________
#stworzyc słownik `{ 'first': funkcja1, 'second': funkcja2 }`, wczytać przez `sys.argv` klucz, wywołać funkcję

from

if __name__ == '__main__':
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
