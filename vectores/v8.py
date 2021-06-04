'''
    Escribir un programa que dé valores a un vector de números enteros, cree un vector
    resultado de multiplicar cada valor leído por el subíndice correspondiente e imprima este
    último vector.
'''

vector = list()

tamaño = int(input('Ingrese el tamaño del vector: '))
if tamaño <= 0:
    print('El tamaño no puede ser menor o igual a 0')
    quit()

for x in range(0, tamaño):
    num = int(input('Ingrese el numero: '))
    vector.append(num)


vector_resultado = []

for num in vector:
    vector_resultado.append(num * (vector.index(num) + 1))

print(f'El vector resultado es: {vector_resultado}')