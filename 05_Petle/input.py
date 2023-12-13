n = int(input("Podaj liczbę:"))
print(f'Podałeś liczbę {n}')

number = input()
suma = 0
for char in str(number):
    print(f"to jest znak->- {char} \n to jest {suma}")
    suma += int(char)
print(suma)
