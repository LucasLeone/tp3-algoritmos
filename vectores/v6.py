'''
    Escribir la media de los elementos que se encuentran en las posiciones pares y la
    media de los elementos que se encuentran en las posiciones impares de un vector
    numérico.
'''

vector = list()

tamaño = int(input('Ingrese el tamaño del vector: '))
if tamaño <= 0:
    print('El tamaño no puede ser menor o igual a 0')
    quit()

for x in range(0, tamaño):
    num = int(input('Ingrese el numero: '))
    vector.append(num)

vector_par = []
vector_impar = []

for i in range(0, tamaño):
    if i % 2 == 0:
        vector_par.append(vector[i])
    else:
        vector_impar.append(vector[i])

media_par = (sum(vector_par) / len(vector_par))
media_impar = (sum(vector_impar) / len(vector_impar))

print(f'La media del vector par es: {media_par}')
print(f'La media del vector impar es: {media_impar}')