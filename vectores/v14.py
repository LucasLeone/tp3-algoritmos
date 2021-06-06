'''
    Escribir un programa que lea un número entero positivo y cuente el número de
    dígitos distintos de que consta.
'''

num = int(input('Ingrese el numero entero positivo: '))

if num < 0:
    print('El numero ingresado no es positivo')
    quit()

num = str(num)

vector = []

for x in num:
    x = int(x)
    vector.append(x)

print(f'Los digitos son: {vector} y consta de {len(vector)} digitos')