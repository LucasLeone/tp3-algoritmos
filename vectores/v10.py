'''
    Escribir un programa que lea un vector de números enteros (de una sola cifra) y
    compruebe si el Número formado por cada uno de los elementos del vector es capicúa o
    no.
'''

vector = list()

tamaño = int(input('Ingrese el tamaño del vector: '))
if tamaño <= 0:
    print('El tamaño no puede ser menor o igual a 0')
    quit()

for x in range(0, tamaño):
    num = int(input('Ingrese el numero: '))
    if num >= 10 or num <= -10:
        pass
    else:
        vector.append(num)



print(vector)