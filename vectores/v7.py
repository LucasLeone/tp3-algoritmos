'''
    Escribir un programa que lea un vector de N enteros y halle 
    la posición del elemento que contiene el valor máximo.
'''

vector = list()

tamaño = int(input('Ingrese el tamaño del vector: '))
if tamaño <= 0:
    print('El tamaño no puede ser menor o igual a 0')
    quit()

for x in range(0, tamaño):
    num = int(input('Ingrese el numero: '))
    vector.append(num)

valor_maximo = max(vector)

print(f'El maximo valor es {valor_maximo} y se encuentra en la posicion {vector.index(valor_maximo) + 1}')