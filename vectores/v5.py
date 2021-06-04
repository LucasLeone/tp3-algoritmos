'''
    Leer un vector de enteros y sacar por pantalla primero todos los
    elementos pares y después todos los impares.
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

for num in vector:
    if num % 2 == 0:
        vector_par.append(num)
    else:
        vector_impar.append(num)

print(f'El vector con valores pares quedo: {vector_par}')
print(f'El vector con valores impares quedo: {vector_impar}')