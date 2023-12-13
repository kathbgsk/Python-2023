import sys


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


if __name__ == '__main__':

    print(sys.argv)
    klucz = (sys.argv[1])
    funkcja = s[klucz]
    funkcja()
    print(klucz)